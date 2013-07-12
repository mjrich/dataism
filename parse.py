import re


def get_count(word_count_tuple):
	"""Returns the count from a dict word/count tuple  -- used for custom sort."""
	return word_count_tuple[1]

def print_ordered_items(item_count):
	items = sorted(item_count.items(), key=get_count, reverse=True)
	for i in items:
		print i


def item_count_dict(tweet_data):
	item_count = {}
	for item in tweet_data:
		# Special case if we're seeing this item for the first time.
		if not item in item_count:
			item_count[item] = 1
		else:
			item_count[item] = item_count[item] + 1
	return print_ordered_items(item_count)

with open('tweets.txt', 'r') as f:
	read_data = f.read()
f.closed


test_string = read_data.lower()

data_match_start = re.findall("data [\w]+", test_string)
data_match_end = re.findall("[\w]+ data", test_string)
data_full_list = data_match_start + data_match_end

item_count_dict(data_full_list)


