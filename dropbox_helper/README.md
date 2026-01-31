# dropbox_helper README

A basic CLI for inspecting files on your dropbox account.

note: the Dropbox API is quite limited - for example, no read access to tags or stars.

## Get API key

- Create an app: https://www.dropbox.com/developers/apps
- Generate an access token
- Set environment variable DROPBOX_TOKEN to that token

## Usage

```
test_list.bat
```

or

```
uv run python -m dropbox_helper list /temp --recursive
```

### Output

```
[DIR ] /temp
[FILE] /temp/spider-portrait.File 26-06-2022, 16 01 24.jpeg
```
