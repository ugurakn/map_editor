# map_editor
a map/level editor that can be used for making pygame platformer games.  
creates map data by saving the placement of on-screen objects into a numpy array.
the array is originally an array of zeros which is filled with other numbers that represent the coordinates of objects to be drawn onto the screen.  
keeps map data in a txt file (maps.txt) which can be converted back into an array with str_to_array module.
