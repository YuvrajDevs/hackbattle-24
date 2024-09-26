import os

# Define the main directory
main_dir = './test_dataset'

# Iterate through each subdirectory (pose)
for pose_dir in os.listdir(main_dir):
    pose_path = os.path.join(main_dir, pose_dir)
    
    # Check if it's a directory
    if os.path.isdir(pose_path):
        # Get all image files in the subdirectory
        image_files = [f for f in os.listdir(pose_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        
        # Sort the files to ensure consistent naming
        image_files.sort()
        
        # Rename the files
        for i, old_name in enumerate(image_files, start=1):
            old_path = os.path.join(pose_path, old_name)
            new_name = f"{i}.png"
            new_path = os.path.join(pose_path, new_name)
            
            # Rename the file
            os.rename(old_path, new_path)
            print(f"Renamed {old_path} to {new_path}")

print("Renaming complete!")