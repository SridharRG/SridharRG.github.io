#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import itertools
import subprocess as sp
import pathlib
import asyncio

HEADER = """<h1 align="left">Personal Wiki</h1>
> A second brain, a humble repository where I gather and preserve everything I learn—raw, unfiltered, and striving for clarity amidst the currents of thought.
"""

INDEX_HEADER = """<h1 align="left">Personal Wiki</h1>

> A second brain, a humble repository where I gather and preserve everything I learn—raw, unfiltered, and striving for clarity amidst the currents of thought.


"""

SUMMARY_HEADER = """# Table of contents


"""

# FOOTER = """## About

# A personal wiki is a digital space where you can organize, store, and manage your knowledge, thoughts, and ideas. It serves as a customizable, accessible repository for information that you can continuously expand and refine. Whether you're documenting your learning journey, managing projects, tracking personal growth, or just storing interesting facts, a personal wiki acts as your second brain or knowledge base.
# """


async def get_category_list():
    """
    Walk the current directory and get a list of all subdirectories at that
    level.  These are the "categories" of TILs.
    """
    avoid_dirs = [
        "images",
        "stylesheets",
        "javascripts",
        "draft",
        "_layouts",
        ".sass-cache",
        "_site",
        ".vitepress",
        "node_modules",
        "public",
    ]
    dirs = [
        x
        for x in os.listdir(".")
        if os.path.isdir(x) and ".git" not in x and x not in avoid_dirs
    ]
    return dirs


def get_title(til_file):
    """
    Read the file until we hit the first line that starts with a #
    indicating a title in markdown.
    """
    with open(til_file) as file:
        for line in file:
            line = line.strip()
            if line.startswith("#"):
                # print(line[1:])
                return line[1:].lstrip()  # text after # and whitespace


def get_tils(category):
    """
    For a given category, get the list of TIL titles
    """
    til_files = [x for x in os.listdir(category)]
    titles = []
    for filename in til_files:
        fullname = os.path.join(category, filename)
        if (os.path.isfile(fullname)) and fullname.endswith(".md"):
            title = get_title(fullname)
            # changing path separator for Windows paths
            # https://mail.python.org/pipermail/tutor/2011-July/084788.html
            titles.append((title, fullname.replace(os.path.sep, "/")))
    return titles


def get_category_dict(category_names):
    categories = {}
    count = 0
    for category in category_names:
        titles = get_tils(category)
        categories[category] = titles
        count += len(titles)
    return (count, categories)


def read_file(filename):
    with open(filename) as file:
        return file.read()


async def create_gitbooks_summary(category_names, categories):
    """
    Create SUMMARY.md for GitBooks site
    """
    print("Generating SUMMARY.md")
    with open("SUMMARY.md", "w") as summary:
        summary.write(SUMMARY_HEADER)
        for category in sorted(category_names):
            summary.write("\n\n## {0}\n\n".format(category.replace("-", " ").title()))
            tils = categories[category]
            summary.write("<ul>")
            for (title, filename) in sorted(tils):
                summary.write("\n<li>")
                summary.write(f"""<a href="{filename}">{title}</a></li>""")
            summary.write("\n")
            summary.write("</ul>")


async def create_til_count_file(count):
    """
    Used by shields.io for generating the TILs count badge on GitHub
    """
    print("Generating count.json")
    with open("count.json", "w") as json_file:
        data = {"count": count}
        json.dump(data, json_file, indent=" ")


async def create_readme(category_names, categories):
    """
    Generate the README.md for github repo
    """
    host_url = "https://github.com/Bhupesh-V/til/blob/master/"
    print("Generating README.md")

    num_columns = 3  # Number of columns for the grid
    num_rows = (len(category_names) + num_columns - 1) // num_columns  # Calculate the number of rows

    category_names = sorted(category_names)

    with open("README.md", "w") as file:
        file.write(HEADER)
        file.write("""\n\n## Categories\n""")

        # Generate the table header
        file.write('<table align="center">\n')

        # Generate the table rows
        for row in range(num_rows):
            file.write("<tr>\n")
            for col in range(num_columns):
                index = row * num_columns + col
                if index < len(category_names):
                    category = category_names[index]
                    tils = categories[category]
                    file.write(f"""<td><a href="#{category.replace(' ', '-').lower()}">{category.replace("-", " ").title()}</a><sup>[{len(tils)}]</sup></td>\n""")
                else:
                    file.write("<td></td>\n")  # Empty cell if no category
            file.write("</tr>\n")

        file.write("</table>\n")

        if len(category_names) > 0:
            file.write("""\n---\n\n""")
            # print the section for each category
        for category in sorted(category_names):
            file.write("\n\n\n### {0}\n\n".format(category.replace("-", " ").title()))
            tils = categories[category]
            file.write("<ul>")
            for (title, filename) in sorted(tils):
                file.write("\n<li>")
                file.write(
                    f"""<a target="_blank" href="{host_url+filename}">{title}</a></li>"""
                )
            file.write("\n")
            file.write("</ul>\n\n")

        # file.write(FOOTER)


async def create_recent_tils_file(categories):
    """
    Generate recent_tils.json to be used by my website & github profile readme
    """

    print("Generating recent_tils.json")
    cmd = "git log --no-color --date=format:'%d %b, %Y' --diff-filter=A --name-status --pretty=''"
    recent_tils = []

    result = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = result.communicate()
    clean_output = out.decode("utf-8").strip("\n").replace("A\t", "").split("\n")
    # filter filepaths that don't exist
    clean_output = [path.lower() for path in clean_output]
    flattened_list = list(itertools.chain(*list(categories.values())))
    flattened_list = [item[1] for item in flattened_list]
    valid_files = list(
        filter(
            lambda path: pathlib.Path(path.lower()).exists() and path in flattened_list,
            clean_output,
        )
    )

    for til in valid_files[:10]:
        til_dict = {}
        til_dict["title"] = get_title(til)
        til_dict["url"] = f"https://til.bhupesh.me/{til[:til.rfind('.')].lower().replace(' ', '-')}"
        recent_tils.append(til_dict)

    with open("recent_tils.json", "w") as json_file:
        json.dump(recent_tils, json_file, ensure_ascii=False, indent=" ")

async def create_index_md(category_names, categories):
    """
    Generate the index.md for the VitePress site
    """
    host_url = "/"
    print("Generating vitepress index.md")

    num_columns = 3  # Number of columns for the grid
    num_rows = (len(category_names) + num_columns - 1) // num_columns  # Calculate the number of rows

    category_names = sorted(category_names)

    with open("index.md", "w") as file:
        file.write(INDEX_HEADER)
        file.write("""\n\n## Categories\n""")

        # Generate the table header
        file.write('<table align="center">\n')
        file.write("<tbody>\n")
        # Generate the table rows
        for row in range(num_rows):
            file.write("<tr>\n")
            for col in range(num_columns):
                index = row * num_columns + col
                if index < len(category_names):
                    category = category_names[index]
                    tils = categories[category]
                    file.write(f"""<td><a href="#{category.replace(' ', '-').lower()}">{category.replace("-", " ").title()}</a><sup>[{len(tils)}]</sup></td>\n""")
                else:
                    continue
                    # file.write("<td></td>\n")  # Empty cell if no category
            file.write("</tr>\n")
        file.write("</tbody>\n")
        file.write("</table>\n")

        if len(category_names) > 0:
            file.write("""\n---\n\n""")
            # print the section for each category
        for category in sorted(category_names):
            file.write("\n\n\n### {0}\n\n".format(category.replace("-", " ").title()))
            tils = categories[category]
            file.write("<ul>")
            for (title, filename) in sorted(tils):
                text = filename.split('/')[1].replace('.md', '')  # Get the filename and remove '.md'
                text = text.replace('_', ' ').title()  # Replace underscores with spaces and convert to title case
                file.write("\n<li>")
                file.write(
                    f"""<a href="{host_url+filename.replace('.md', '')}">{text}</a></li>"""
                )
            file.write("\n")
            file.write("</ul>\n\n")

        # file.write(FOOTER)

async def create_sidebar_config(category_names):
    """
    Generate the sidebar configuration for VitePress
    """
    print("Generating vitepress sidebar config")
    sidebar_config = []

    for category in sorted(category_names):
        items = []
        tils = get_tils(category)
        for (title, filename) in sorted(tils):
            text = filename.split('/')[1].replace('.md', '')  # Get the filename and remove '.md'
            text = text.replace('_', ' ').title()  # Replace underscores with spaces and convert to title case
            items.append({
                # "text": filename.split('/')[1].replace('.md', '').replace('_', ' '),
                "text": text,
                "link": f"/{filename.replace('.md', '')}"
            })
        sidebar_config.append({
            "text": category.replace("-", " ").title(),
            "items": items
        })

    with open(".vitepress/sidebar.js", "w") as sidebar_file:
        sidebar_file.write("export const sidebar = ")
        json.dump(sidebar_config, sidebar_file, indent=2)

async def main():
    """
    TIL Build Script Algorithm:

    1. Get list of directories
    2. For each valid TIL category, find markdown files inside it
    3. Generate recent_tils using git
    4. Generate SUMMARY.md for gitbook
    5. Generate README.md for GitHub
    """

    get_categories = asyncio.create_task(get_category_list())
    category_names = await get_categories
    count, categories = get_category_dict(category_names)

    task1 = asyncio.create_task(create_recent_tils_file(categories))
    # task2 = asyncio.create_task(create_readme(category_names, categories))
    # task3 = asyncio.create_task(create_gitbooks_summary(category_names, categories))
    task4 = asyncio.create_task(create_til_count_file(count))
    task5 = asyncio.create_task(create_index_md(category_names, categories))
    task6 = asyncio.create_task(create_sidebar_config(category_names))

    await task1
    # await task2
    # await task3
    await task4
    await task5
    await task6

    print(count, "TILs read")


asyncio.run(main())
