#!/usr/bin/python3
"""
Task 00: Simple templating program.

generate_invitations(template, attendees):
- template: string containing placeholders {name}, {event_title}, {event_date}, {event_location}
- attendees: list of dictionaries
Creates output_1.txt, output_2.txt, ... with placeholders replaced.
Missing/None values become "N/A".

Error handling:
- Empty template -> "Template is empty, no output files generated."
- Empty attendees -> "No data provided, no output files generated."
- Invalid types -> log an error indicating invalid input type(s), then return.
"""

from __future__ import annotations


def _is_list_of_dicts(obj):
    """Return True if obj is a list and every element is a dict."""
    if not isinstance(obj, list):
        return False
    return all(isinstance(item, dict) for item in obj)


def generate_invitations(template, attendees):
    """
    Generate invitation files from template and attendees list.

    Output files: output_1.txt ... output_N.txt
    """
    # Type checks
    if not isinstance(template, str):
        print(
            "Invalid input type: template must be a string, got "
            f"{type(template).__name__}."
        )
        return

    if not _is_list_of_dicts(attendees):
        got = type(attendees).__name__
        print(
            "Invalid input type: attendees must be a list of dictionaries, got "
            f"{got}."
        )
        return

    # Empty checks
    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    placeholders = ("name", "event_title", "event_date", "event_location")

    for idx, attendee in enumerate(attendees, start=1):
        # Prepare safe values with N/A fallback (missing key or None)
        values = {}
        for key in placeholders:
            val = attendee.get(key, "N/A")
            if val is None:
                val = "N/A"
            values[key] = str(val)

        output_text = template
        for key in placeholders:
            output_text = output_text.replace("{" + key + "}", values[key])

        filename = f"output_{idx}.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(output_text)
        except OSError as exc:
            # Graceful fail per hint; do not crash the program.
            print(f"Error writing file {filename}: {exc}")
