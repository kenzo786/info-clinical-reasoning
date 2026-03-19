param(
    [string]$InputXml = "clinicalreasoningknowledgebase.WordPress.2026-02-28.xml",
    [string]$OutputDir = "extracted-illness-scripts"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Convert-SlugToTitle {
    param([string]$Slug)
    $base = $Slug -replace '^is-', ''
    if ([string]::IsNullOrWhiteSpace($base)) { return $Slug }
    $words = $base -split '-'
    $titled = foreach ($w in $words) {
        if ($w.Length -eq 0) { continue }
        if ($w.Length -eq 1) { $w.ToUpper() } else { $w.Substring(0, 1).ToUpper() + $w.Substring(1) }
    }
    return ($titled -join ' ')
}

function Get-ConditionName {
    param(
        [string]$Html,
        [string]$Slug
    )
    $titleDivMatch = [regex]::Match($Html, '(?is)<div\s+id="illness-script-title">(.*?)</div>')
    if ($titleDivMatch.Success) {
        $raw = $titleDivMatch.Groups[1].Value
        $raw = [regex]::Replace($raw, '\[sc\s+name="ask-ai-100".*?\[/sc\]', '', 'IgnoreCase')
        $raw = [regex]::Replace($raw, '<[^>]+>', '')
        $raw = [regex]::Replace($raw, '\s*Illness\s+Script\s*$', '', 'IgnoreCase')
        $raw = [regex]::Replace($raw, '\s+', ' ').Trim()
        if (-not [string]::IsNullOrWhiteSpace($raw)) {
            return $raw
        }
    }
    return (Convert-SlugToTitle -Slug $Slug)
}

function Find-DetailsBlockEnd {
    param(
        [string]$Text,
        [int]$OpenDetailsIndex
    )
    $tokenRegex = [regex]::new('(?is)<details\b|</details>')
    $matches = $tokenRegex.Matches($Text, $OpenDetailsIndex)
    if ($matches.Count -eq 0) {
        return -1
    }

    $depth = 0
    $seenOpen = $false
    foreach ($m in $matches) {
        if ($m.Value -match '^<details\b') {
            $depth += 1
            $seenOpen = $true
            continue
        }

        if ($seenOpen) {
            $depth -= 1
            if ($depth -eq 0) {
                return ($m.Index + $m.Length)
            }
        }
    }
    return -1
}

function Normalize-SummaryLabel {
    param(
        [string]$InnerText,
        [string]$Condition
    )
    $label = $InnerText
    $label = [regex]::Replace($label, '\[sc\s+name="ask-ai-\d+"\s+Q=".*?"\]\[/sc\]', '', 'IgnoreCase')
    $label = [regex]::Replace($label, '\s+', ' ').Trim()
    $label = [regex]::Replace($label, '^' + [regex]::Escape($Condition) + '\s+', '', 'IgnoreCase').Trim()
    $label = [regex]::Replace($label, '^Epidemiology,\s*Risk\s*Factors\s*&\s*Prevention$', 'Epidemiology', 'IgnoreCase')
    return $label
}

function AddOrReplaceSummaryId {
    param(
        [string]$SummaryTag,
        [int]$SectionNumber,
        [int]$AskAiNumber,
        [string]$Condition
    )
    $match = [regex]::Match($SummaryTag, '(?is)^<summary\b(?<attrs>[^>]*)>(?<inner>.*?)</summary>$')
    if (-not $match.Success) {
        return $SummaryTag
    }

    $attrs = $match.Groups['attrs'].Value
    $inner = $match.Groups['inner'].Value
    $label = Normalize-SummaryLabel -InnerText $inner -Condition $Condition

    $attrsNoId = [regex]::Replace($attrs, '\s+\bid\s*=\s*"[^"]*"', '')
    $attrsNoId = [regex]::Replace($attrsNoId, '^\s+|\s+$', '')
    if ([string]::IsNullOrWhiteSpace($attrsNoId)) {
        $attrsOut = ' id="s-is.' + $SectionNumber + '.0"'
    } else {
        $attrsOut = ' ' + $attrsNoId + ' id="s-is.' + $SectionNumber + '.0"'
    }

    return '<summary' + $attrsOut + '>' + $label + ' [sc name="ask-ai-' + $AskAiNumber + '" Q="' + $Condition + '"][/sc]</summary>'
}

if (-not (Test-Path -LiteralPath $InputXml)) {
    throw "Input XML not found: $InputXml"
}

$xmlText = [System.IO.File]::ReadAllText((Resolve-Path -LiteralPath $InputXml), [System.Text.Encoding]::UTF8)

$itemRegex = [regex]::new('(?is)<item>.*?<title><!\[CDATA\[(?<slug>is-[^\]]+)\]\]></title>.*?<content:encoded><!\[CDATA\[(?<content>.*?)\]\]></content:encoded>.*?</item>')
$itemMatches = $itemRegex.Matches($xmlText)

$excludedSlugs = @(
    "is-closed-01",
    "is-open-start-01",
    "is-open-end-01",
    "is-test"
)

$processed = 0
$skipped = @()
$totalIsItems = 0

if (-not (Test-Path -LiteralPath $OutputDir)) {
    New-Item -ItemType Directory -Path $OutputDir | Out-Null
}

foreach ($item in $itemMatches) {
    $slug = $item.Groups["slug"].Value
    $content = $item.Groups["content"].Value
    $totalIsItems += 1

    if ($excludedSlugs -contains $slug) {
        $skipped += [pscustomobject]@{
            slug = $slug
            reason = "excluded_slug"
        }
        continue
    }

    if ($content -notmatch 'id="c-is\.13\.0"') {
        $skipped += [pscustomobject]@{
            slug = $slug
            reason = "missing_c-is.13.0"
        }
        continue
    }

    $condition = Get-ConditionName -Html $content -Slug $slug

    $titleDivMatch = [regex]::Match($content, '(?is)<div\s+id="illness-script-title">.*?</div>')
    $startIndex = 0
    if ($titleDivMatch.Success) {
        $startIndex = $titleDivMatch.Index
    }

    $c13Open = [regex]::Match($content, '(?is)<details\b[^>]*\bid="c-is\.13\.0"[^>]*>')
    if (-not $c13Open.Success) {
        $skipped += [pscustomobject]@{
            slug = $slug
            reason = "cannot_find_c-is.13.0_opening"
        }
        continue
    }

    $endIndex = Find-DetailsBlockEnd -Text $content -OpenDetailsIndex $c13Open.Index
    if ($endIndex -lt 0) {
        $skipped += [pscustomobject]@{
            slug = $slug
            reason = "cannot_find_c-is.13.0_closing"
        }
        continue
    }

    if ($endIndex -le $startIndex) {
        $skipped += [pscustomobject]@{
            slug = $slug
            reason = "invalid_extraction_range"
        }
        continue
    }

    $segment = $content.Substring($startIndex, $endIndex - $startIndex)

    $missingRequired = $false
    for ($i = 1; $i -le 13; $i++) {
        if ($segment -notmatch ('id="c-is\.' + $i + '\.0"')) {
            $missingRequired = $true
            break
        }
    }
    if ($missingRequired) {
        $skipped += [pscustomobject]@{
            slug = $slug
            reason = "missing_required_c-is_sections"
        }
        continue
    }

    if (-not $titleDivMatch.Success) {
        $insertedTitleDiv = '<div id="illness-script-title">' + $condition + ' [sc name="ask-ai-100" Q="' + $condition + '"][/sc]</div>'
        $segment = $insertedTitleDiv + "`r`n`r`n" + $segment
    }

    $seenSections = New-Object 'System.Collections.Generic.HashSet[int]'
    $segment = [regex]::Replace(
        $segment,
        '(?is)(<details\b[^>]*\bid="c-is\.(?<n>[1-9]|1[0-3])\.0"[^>]*>\s*)(?<summary><summary\b[^>]*>.*?</summary>)',
        {
            param($m)
            $n = [int]$m.Groups["n"].Value
            [void]$seenSections.Add($n)
            $ask = if ($n -eq 13) { 115 } else { 100 + $n }
            $newSummary = AddOrReplaceSummaryId -SummaryTag $m.Groups["summary"].Value -SectionNumber $n -AskAiNumber $ask -Condition $condition
            return $m.Groups[1].Value + $newSummary
        }
    )

    if ($seenSections.Count -lt 13) {
        $skipped += [pscustomobject]@{
            slug = $slug
            reason = "missing_top_level_summary_for_required_section"
        }
        continue
    }

    $outputPath = Join-Path $OutputDir ($slug + ".html")
    $utf8NoBom = New-Object System.Text.UTF8Encoding($false)
    [System.IO.File]::WriteAllText($outputPath, $segment, $utf8NoBom)
    $processed += 1
}

$report = [pscustomobject]@{
    input_xml = (Resolve-Path -LiteralPath $InputXml).Path
    output_dir = (Resolve-Path -LiteralPath $OutputDir).Path
    total_is_items = $totalIsItems
    processed = $processed
    skipped = $skipped.Count
    skipped_items = $skipped
    generated_at_utc = (Get-Date).ToUniversalTime().ToString("o")
}

$reportPath = Join-Path $OutputDir "extraction-report.json"
$report | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $reportPath -Encoding utf8

Write-Host "Processed: $processed"
Write-Host "Skipped: $($skipped.Count)"
Write-Host "Output directory: $OutputDir"
Write-Host "Report: $reportPath"
