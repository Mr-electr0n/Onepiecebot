def are_coordinates_unique_among_all(existing_data, new_coords):
    '''This function checks if the new global coordinates are unique among all existing data.'''
    for server_info in existing_data:
        # Check if new global coordinates match existing data
        if 'global_cod' in server_info:
            existing_global_coords = server_info['global_cod']
            if existing_global_coords == new_coords['global_cod']:
                return False
    return True


from database import collection_name as dataset , reserved_collection_name as col
# Define the dimensions of the port, market, town, and palace
port_dim = (30, 10)
market_dim = (10, 10)
town_dim = (20, 10)
palace_dim = (5, 5)

def add_parts_to_island(server_id):
    cordtaa = col.find_one({"_id": "local_locations"})
    coordinate = cordtaa['locations']
    # Define a function to check if a part fits on the island
    def check_fit(part_dim, island_data = coordinate):
        # Get the boundary and inside coordinates of the island
        boundary_coords = island_data["boundaries_coordinates"]
        inside_coords = island_data["island_coordinates"]

        # Get the width and height of the part
        part_width, part_height = part_dim

        # Loop through all possible positions of the part on the island
        for x in range(0, 50 - part_width + 1):
            for y in range(0, 50 - part_height + 1):
                # Create a list of coordinates for the part
                part_coords = []
                for i in range(x, x + part_width):
                    for j in range(y, y + part_height):
                        part_coords.append({"x": i, "y": j})

                # Check if the part overlaps with the boundary or any existing parts
                if not any(coord in boundary_coords for coord in part_coords) and not any(coord in inside_coords for coord in part_coords):
                    # Return the position and coordinates of the part
                    return (x, y), part_coords

        # Return None if no fit is found
        return None

    # Define a function to add a part to the island
    def add_part(part_name, part_dim, island_data):
        # Check if the part fits on the island
        result = check_fit(part_dim, island_data)
        if result is not None:
            # Get the position and coordinates of the part
            position, coordinates = result

            # Update the inside coordinates of the island to include the part
            island_data["island_coordinates"].extend(coordinates)

            # Create a document for the part with its name, position, and coordinates
            part_doc = {
                "name": part_name,
                "position": position,
                "coordinates": coordinates
            }

            # Return the part document
            return part_doc
        else:
            # Return None if the part cannot be added
            return None

    # Find the document for the island data in the Reserved_data collection using {"_id": "local_locations"} as the filter
    island_data = col.find_one({"_id": "local_locations"})

    # Create an empty list to store the parts data
    parts_list = []

    # Add the port, market, town, and palace to the island
    parts_list.append(add_part("port", port_dim, island_data))
    parts_list.append(add_part("market", market_dim, island_data))
    parts_list.append(add_part("town", town_dim, island_data))
    parts_list.append(add_part("palace", palace_dim, island_data))

    # Filter out None values from the list (parts that couldn't be added)
    parts_list = [part for part in parts_list if part is not None]

    # Update the MongoDB collection with the parts data
    dataset.update_one({"_id":server_id}, {"$set": {"parts": parts_list}})

    # Print a success message or any other desired action
    print("Updated parts for the island")

# Call the function to add parts to the island

