# Primary-Care Minor-Illness Markmap Shortcode Template

Use the staged `pcmi-*` maps as the working pattern.

## Rule

For a new staged map, the only value you should need to replace manually is `POST_ID`, once the paired reference has a live post ID.

## Core Pattern

1. Use `s-is.xxx` anchors in the paired reference HTML.
2. Use `map-steps-and-links` for each top-level map section.
3. Use `link-websheet` for child items that should deep-link into the paired reference.
4. Keep the map shorter than the reference.
5. Keep the section colors and step order stable:
   - `101` green
   - `102` green
   - `103` purple
   - `104` yellow
   - `105` yellow
   - `106` pink
   - `107` yellow
   - `108` purple
   - `109` pink
   - `110` blue
   - `111` blue

## WordPress Content Header

```md
[sc name="map-yaml" title="TOPIC" id="POST_ID"][/sc]
```

Use this shortcode header for anything you plan to paste directly into WordPress content. Do not use YAML front matter for the WordPress copy.

## Section Template

```md
[sc name="map-steps-and-links" id="POST_ID" anchor="101" title="Overview" color="green" step="1" info-modal="" pathway="display-none" youtube="display-none"][/sc]<details class="kb-accordion kb-parent d-green" open> <summary id="s-is.101" role="button">Overview</summary> <ul> <li><strong>Clinical challenge:</strong> ...</li> <li><strong>Guideline frame:</strong> ...</li> <li><strong>Core stance:</strong> ...</li> </ul> </details>
```

## Child-Link Template

```md
<li>[sc name="link-websheet" id="POST_ID" anchor="104.1"][/sc]<strong>Key question</strong>: why it matters in brief.</li>
```

## Working Examples

- `primary-care minor-illness/markmaps/pcmi-acute-cough.md`
- `primary-care minor-illness/markmaps/pcmi-headache.md`
- `primary-care minor-illness/markmaps/pcmi-back-pain.md`
- `primary-care minor-illness/markmaps/pcmi-emergency-hormonal-contraception.md`
- `primary-care minor-illness/markmaps/pcmi-vaginal-thrush.md`
