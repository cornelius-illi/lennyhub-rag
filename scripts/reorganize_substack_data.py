#!/usr/bin/env python3
"""
Reorganize Substack Data Script

This script:
1. Moves all markdown files from subdirectories to the root data directory
2. Updates image links in markdown files to point to the correct attachment paths

Usage:
    python scripts/reorganize_substack_data.py data/cutlefish.substack.com
"""

import re
import shutil
from pathlib import Path
import argparse


def update_image_links(content: str, md_file: Path, data_root: Path) -> str:
    """
    Update image links in markdown content to use correct paths.
    
    Converts relative paths like:
        ![alt](../attachments/image.png)
    To:
        ![alt](attachments/image.png)
    """
    # Pattern to match markdown image syntax
    # Matches: ![alt text](path/to/image.ext)
    image_pattern = re.compile(r'!\[([^\]]*)\]\(([^)]+)\)')
    
    def replace_image_path(match):
        alt_text = match.group(1)
        image_path = match.group(2)
        
        # Skip external URLs
        if image_path.startswith(('http://', 'https://')):
            return match.group(0)
        
        # Normalize the path
        # Remove leading ../ or ./ 
        normalized_path = image_path.lstrip('./')
        while normalized_path.startswith('../'):
            normalized_path = normalized_path[3:]
        
        # Return updated markdown image syntax
        return f'![{alt_text}]({normalized_path})'
    
    updated_content = image_pattern.sub(replace_image_path, content)
    return updated_content


def reorganize_data(data_dir: Path, dry_run: bool = False):
    """
    Reorganize data directory by moving markdown files to root and updating image links.
    
    Args:
        data_dir: Path to the data directory (e.g., data/cutlefish.substack.com)
        dry_run: If True, only print what would be done without making changes
    """
    if not data_dir.exists():
        print(f"Error: Directory {data_dir} does not exist!")
        return
    
    print(f"Reorganizing data in: {data_dir}")
    print("=" * 70)
    
    # Find all markdown files in subdirectories
    md_files = []
    for ext in ['.md', '.markdown']:
        md_files.extend(data_dir.glob(f'**/*{ext}'))
    
    # Filter out files already in root and hidden files
    md_files = [
        f for f in md_files 
        if f.parent != data_dir and not f.name.startswith('.')
    ]
    
    print(f"\nFound {len(md_files)} markdown files in subdirectories")
    
    if len(md_files) == 0:
        print("No files to reorganize!")
        return
    
    # Process each file
    moved_count = 0
    updated_count = 0
    
    for md_file in md_files:
        relative_path = md_file.relative_to(data_dir)
        target_path = data_dir / md_file.name
        
        # Check for name conflicts
        if target_path.exists() and target_path != md_file:
            print(f"\n⚠️  Warning: {md_file.name} already exists in root, skipping...")
            continue
        
        # Read and update content
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Update image links
            updated_content = update_image_links(content, md_file, data_dir)
            
            if dry_run:
                print(f"\n[DRY RUN] Would move: {relative_path} -> {md_file.name}")
                if content != updated_content:
                    print(f"          Would update image links in {md_file.name}")
            else:
                # Write updated content to target location
                with open(target_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                
                # Remove original file if it's different from target
                if md_file != target_path:
                    md_file.unlink()
                
                moved_count += 1
                if content != updated_content:
                    updated_count += 1
                    print(f"✓ Moved and updated: {relative_path} -> {md_file.name}")
                else:
                    print(f"✓ Moved: {relative_path} -> {md_file.name}")
        
        except Exception as e:
            print(f"✗ Error processing {md_file}: {e}")
    
    # Remove empty subdirectories
    if not dry_run:
        for subdir in data_dir.iterdir():
            if subdir.is_dir() and subdir.name not in ['attachments', '.']:
                try:
                    # Only remove if empty
                    if not any(subdir.iterdir()):
                        subdir.rmdir()
                        print(f"\n✓ Removed empty directory: {subdir.name}")
                except OSError:
                    # Directory not empty, skip
                    pass
    
    print("\n" + "=" * 70)
    if dry_run:
        print("DRY RUN COMPLETE - No changes made")
        print(f"Would move {len(md_files)} files")
    else:
        print("REORGANIZATION COMPLETE")
        print(f"Moved: {moved_count} files")
        print(f"Updated image links in: {updated_count} files")


def main():
    parser = argparse.ArgumentParser(
        description="Reorganize Substack data by moving markdown files to root and updating image links"
    )
    parser.add_argument(
        "data_dir",
        type=str,
        help="Path to the data directory (e.g., data/cutlefish.substack.com)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making changes"
    )
    
    args = parser.parse_args()
    
    data_dir = Path(args.data_dir)
    reorganize_data(data_dir, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
