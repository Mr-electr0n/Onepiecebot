from PIL import Image , ImageDraw
import requests
from io import BytesIO
import random
import json
from database import collection_name , reserved_collection_name ,connection_string
from shapely.geometry import Point
from shapely.ops import cascaded_union
import pymongo





# Map dimensions


# for now map is of 10K boxes but i will expand it later on as per the needs 
# i will make a whole systemt manage that in future 

# Reserved area dimensions and top-left corner coordinates
# Function to generate a random location for a server   

# Initialize a list to store the coordinates


#test this funtion for me

generated_coordinates = []
def local_location(setts, local_height=10000, local_breath=10000):
    global generated_coordinates

    # Create a buffer around the previously generated coordinates
    if generated_coordinates:
        buffer_distance = 150  #will be giving it a range in future 
        buffer_polygons = [Point(coord).buffer(buffer_distance) for coord in generated_coordinates]
        buffer_union = cascaded_union(buffer_polygons)
    else:
        buffer_union = None

    # Generate coordinates until unique coordinates are found
    while True:
        x_coordinate = random.randint(0, local_breath)
        y_coordinate = random.randint(0, local_height)
        new_coordinate = (x_coordinate, y_coordinate)
        
        # Check if coordinates already exist in the buffer
        if buffer_union is None or not buffer_union.contains(Point(new_coordinate)):
            break

    # Add the new coordinates to the list
    generated_coordinates.append(new_coordinate)
    
    # Store the new coordinates in the MongoDB collection
    try:
        reserved_collection_name.update_one({"_id": "local_locations"}, {"$push": {"locations": {"$each":new_coordinate}}})
    except Exception as e:
        print(f"Error storing coordinates in MongoDB: {str(e)}")


















#insted of fetching the server image from database i can just get it from discord.py 
def design_map(server_id):

    try:

            # Fetch the server info from the server_info collection
            server_info = collection_name.find_one({'_id':server_id})

            if server_info is not None:
                # Get the image URL and coordinates
                server_pfp_url = server_info['guild_pfp']
                serverX1, serverY1 = server_info['server_coordinate']['x_coordinate_1'], server_info['local_cod']['y_coordinate_1']
                nearest_local = server_info['server_coordinate']

                # Open the first image
                image1 = Image.open("E:\\ONEPIECEBOT\\IMAGES\\clear.jpg")

                # Download the server icon image from the URL
                response = requests.get(server_pfp_url)
                server_icon = Image.open(BytesIO(response.content))

                # Calculate the new siy_coordinatee for the server icon image
                server_icon_new_siy_coordinatee = (int(image1.siy_coordinatee[0] * 0.2), int(image1.siy_coordinatee[1] * 0.1))

                # Resiy_coordinatee the server icon image
                server_icon = server_icon.resiy_coordinatee(server_icon_new_siy_coordinatee)
                server_icon = server_icon.convert("RGBA")

                # Calculate the position for centering the icon around the dots
                icon_x_position = serverX1 - server_icon_new_siy_coordinatee[0] // 2
                icon_y_position = serverY1 - server_icon_new_siy_coordinatee[1] // 2

                # Paste the server icon image onto the map
                image1.paste(server_icon, (icon_x_position, icon_y_position), server_icon)

                # Add lines with unique colors and print dot numbers
                draw = ImageDraw.Draw(image1)
                dot_siy_coordinatee = 5  # Increased dot siy_coordinatee

                # Collect dot coordinates in a list
                dot_coordinates = []
                for local_square_dict in nearest_local:
                    for _, coordinates in local_square_dict.items():
                        x = coordinates['y_coordinate']
                        y = coordinates['x_coordinate']
                        dot_coordinates.append((x, y))

                # Draw lines with unique colors and print dot numbers
                line_connections = [
                    (0, 1),
                    (1, 2),
                    (2, 4),
                    (4, 7),
                    (7, 6),
                    (6, 5),
                    (5, 3),
                    (3, 0)
                ]

                for start, end in line_connections:
                    x1, y1 = dot_coordinates[start]
                    x2, y2 = dot_coordinates[end]
                    
                    line_color = (0, 0, 0, 255)  # Black color
                    draw.line([(x1, y1), (x2, y2)], fill=line_color, width=2)  # Increase the line width
                    
                    print(f"Line from dot{start} to dot{end}")

                # Save the modified image
                image1.save("E:\\ONEPIECEBOT\\IMAGES\\image_with_colored_lines.png")




    except Exception as e:
        print(f"An error occurred while generating the map: {e}")










