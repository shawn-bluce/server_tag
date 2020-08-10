import iterm2


product_server_origin_map = {
}

product_server_map = {}
for name, host_list in product_server_origin_map.items():
    for host in host_list:
        product_server_map[host] = name


test_server_origin_map = {
}

test_server_map = {}
for name, host_list in test_server_origin_map.items():
    for host in host_list:
        test_server_map[host] = name


# color
product_tab_color = iterm2.Color()
test_tab_color = iterm2.Color()
other_tab_color = iterm2.Color()
