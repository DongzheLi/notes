#!/usr/bin/env python3

import os, csv, time, webbrowser, argparse
from datetime import datetime, timedelta
from pathlib import Path
import markdown
import tempfile


# Constants
NOTES_DIR = "notes"
PROBLEMS_DIR = os.path.join(NOTES_DIR, "problems")
SOLUTIONS_DIR = os.path.join(NOTES_DIR, "solutions")
TMP_DIR = "tmp"
TEMPLATES_DIR = "templates"
LOG_FILE = "log.csv"

# Ratings
RATING = {
    "new": 1,
    "wrong": 1,
    "difficult": 3,
    "medium": 7,
    "easy": 14,
    "trivial": 28
}

def run_review_session():
    pass

def show_statistics():
    pass


def main():
    parser = argparse.ArgumentParser(description="Notes Review")
    parser.add_argument("command", nargs="?", default="review",
                        choices=["review", "stats", "add"],
                        help="Command to execute")
    args = parser.parse_args()
    # setup_directories()
    if args.command == "review":
        run_review_session()
    elif args.command == "stats":
        show_statistics()

