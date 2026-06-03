#!/usr/bin/env python3
import os
import argparse

def generate_site(args):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    index_path = os.path.join(base_dir, "index.html")
    
    if not os.path.exists(index_path):
        print("Error: index.html template not found in this directory.")
        return
        
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Format phone number
    raw_phone = "".join(filter(str.isdigit, args.phone))
    if len(raw_phone) == 10:
        phone_formatted = f"{raw_phone[:3]}-{raw_phone[3:6]}-{raw_phone[6:]}"
        phone_link = f"{raw_phone[:3]}-{raw_phone[3:6]}-{raw_phone[6:]}"
        phone_raw = raw_phone
    else:
        phone_formatted = args.phone
        phone_link = args.phone
        phone_raw = args.phone

    content = content.replace("{{COMPANY_NAME}}", args.company)
    content = content.replace("{{WEBSITE_URL}}", args.website)
    content = content.replace("{{PHONE_FORMATTED}}", phone_formatted)
    content = content.replace("{{PHONE_LINK}}", phone_link)
    content = content.replace("{{PHONE_RAW}}", phone_raw)
    content = content.replace("{{CITY}}", args.city)
    content = content.replace("{{STATE}}", args.state.upper())
    content = content.replace("{{ZIP}}", args.zip if args.zip else "")
    content = content.replace("{{LAT}}", str(args.lat) if args.lat else "")
    content = content.replace("{{LNG}}", str(args.lng) if args.lng else "")

    out_path = os.path.join(base_dir, f"{args.company.replace(' ', '-').lower()}-index.html")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"✅ Successfully generated new generic landing page: {out_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a new universal Locksmith landing page.")
    parser.add_argument("--company", required=True, help="Company Name")
    parser.add_argument("--website", required=True, help="Website Domain (e.g. referencelocksmith.com)")
    parser.add_argument("--city", required=True, help="Target City")
    parser.add_argument("--state", required=True, help="Target State abbreviation")
    parser.add_argument("--phone", required=True, help="Target Phone Number")
    parser.add_argument("--zip", required=False, help="Target ZIP code", default="")
    parser.add_argument("--lat", required=False, help="Target Latitude", default="")
    parser.add_argument("--lng", required=False, help="Target Longitude", default="")
    
    args = parser.parse_args()
    generate_site(args)
