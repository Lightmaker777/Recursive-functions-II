# Recursive functions II
# Task 3:
# A recursive function named count_pages that will count the amount of pages in a website. Takes a single argument as a list of pages, defined as dictionaries that may have two keys: title and pages.

# The first is the title of the page and the second is another list with the same kind of dictionaries (again with title and, possibly, pages). The tree of pages has no depth limitations.

# If a page dictionary has no key pages it means it has no further child pages, but all the pages, including those with children, count as a page.


def count_pages(pages):
    count = 0
    for page in pages:
        count += 1  # Count the current page
        if "pages" in page:
            count += count_pages(page["pages"])  # Recursive call to count child pages
    return count


    
test_data1 = [
    {
        "title": "Home",
        "pages": [
            {
                "title": "About",
                "pages": [
                    {
                        "title": "The company"
                    },
                    {
                        "title": "Our services"
                    },
                    {
                        "title": "Our products"
                    },
                    {
                        "title": "Our deliveries",
                        "pages": [
                            {
                                "title": "National"
                            },
                            {
                                "title": "International"
                            }
                        ]
                    }
                ]
            },
            {
                "title": "Shop",
                "pages": [
                    {
                        "title": "Browse all"
                    },
                    {
                        "title": "Categories"
                    }
                ]
            },
            {
                "title": "My account",
                "pages": [
                    {
                        "title": "Settings"
                    },
                    {
                        "title": "Edit profile"
                    },
                    {
                        "title": "My transactions"
                    }
                ]
            }
        ]
    }
]
print(count_pages(test_data1))