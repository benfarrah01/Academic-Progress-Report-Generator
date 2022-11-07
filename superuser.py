def compare_to_super_user(data, apr):
	for row in data:
		for i in row:
			i += (i+1)
            superuser = data[1]
			if i/superuser > .7:
                return apr
