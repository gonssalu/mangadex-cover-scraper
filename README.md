# mangadex-cover-scraper

A Python script to download all the cover images from a mangadex entry. Supports multiple locales.

## Usage

**Run this command** in the directory you want the covers to be downloaded to:
`python3 covers.py <mangadex_id> [locale]`

The covers will be downloaded to a folder named after the manga's id.
If the locale is not specified, the script will download the covers for all the locales.

The cover file name will follow this pattern:
`<mangadex_entry_id>/Volume <volume_number> [<locale>].jpg`
<span style="font-size: 12px; margin-left: 5px;">The volume number will have leading zeros up until 2 digits.</span>

#### Example

<span style="font-size: 14px;">Download all the english covers for a mangadex entry:</span>
`python3 covers.py 9f39246a-8b05-4b19-b822-727e748723dc en`

<span style="font-size: 14px;">Download all the covers for a mangadex entry:</span>
`python3 covers.py 9f39246a-8b05-4b19-b822-727e748723dc`
