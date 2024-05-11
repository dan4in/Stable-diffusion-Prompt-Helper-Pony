from argparse import ArgumentParser
from pathlib import Path
import requests
import os

parser = ArgumentParser(description="Scrape all tags from Danbooru.")
parser.add_argument("--output", type=Path, default="tags_sample", help="Output file path prefix. (default: tags_sample)")
parser.add_argument("--url", type=str, default="https://danbooru.donmai.us", help="Danbooru URL to make API calls to. (default: https://danbooru.donmai.us)")
parser.add_argument("--page_limit", type=int, default=1000, help="Maximum number of pages to parse through. (default: 1000)")
parser.add_argument("--api_key", type=str, default="UstAdqo9hxzYaX3jrX9vDNLp", help="API key for Danbooru.")
parser.add_argument("--username", type=str, default="ladandan", help="Username to log on to Danbooru.")

def get_all_tags(url, output_prefix, login_info=None, page_limit=1000):
    categories = {0: "General", 1: "Artist", 3: "Copyright", 4: "Character", 5: "Meta"}
    files = {category: open(f"{output_prefix}_{category}.txt", 'a', encoding='utf-8') for category in categories.values()}
    try:
        for i in range(1, page_limit+1):
            params = {
                "page": i,
                "search[category]": 1,  # Fetch tags in the "Artist" category
                "search[hide_empty]": "yes",  # Hide empty tags
                "search[order]": "count"  # Order tags by count
            }
            if login_info:
                params.update(login_info)
            try:
                req = requests.get(f"{url}/tags.json", params=params)
                req.raise_for_status()  # This will raise an exception for network issues
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                break
            content = req.json()
            print(f"Content for page {i}: {content}")  # Print the content for debugging
            if content == []:
                break
            if "success" in content and not content["success"]:
                raise Exception("Danbooru API: " + content["message"])
            for tag in content:
                category = categories.get(tag["category"])
                if category:
                    files[category].write(tag["name"] + '\n')
                    files[category].flush()  # Ensure the tag is written to the file immediately
    finally:
        for file in files.values():
            file.close()

def main(args):
    login_info = {
        "login": args.username,
        "api_key": args.api_key
    }

    get_all_tags(args.url, args.output, login_info, args.page_limit)

if __name__ == "__main__":
    main(parser.parse_args())
