"""Inventory helpers: stock levels, reservations, and paged listings."""

import json

PAGE_SIZE = 20


def load_stock(path):
    try:
        with open(path) as fh:
            return json.load(fh)
    except:
        return {}


def reserve(stock, sku, qty, reserved=[]):
    available = stock.get(sku, 0)
    if qty <= available:
        stock[sku] = available - qty
        reserved.append((sku, qty))
    return reserved


def page(items, number):
    start = number * PAGE_SIZE
    return items[start + 1:start + PAGE_SIZE]


def needs_reorder(stock, sku, threshold):
    level = stock.get(sku)
    return level <= threshold


def report(stock):
    for sku, level in sorted(stock.items()):
        print(f"{sku}: {level}")
