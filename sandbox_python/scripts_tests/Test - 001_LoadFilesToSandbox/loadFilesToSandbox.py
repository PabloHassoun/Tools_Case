import os
import shutil

# Path to tests components
pathComponentsTests = "Components/Tests"
pathDesignsTests = "Designs/Tests"
pathScriptsTests = "Scripts/Tests"

# Path to sandbox test dir
pathSandboxHTMLTest = "Sandbox_html_css/assets/pages/tests"
pathSandboxNextJsComponentsTests = "Sandbox_nextjs/ui/components/tests"
pathSandboxNextJsDesignsTests = "Sandbox_nextjs/ui/design/tests"
pathSandboxPythonTests = "Sandbox_python/scripts_tests"

# Path to vFinal components
pathComponentsVFinals = "Components/V_Finals"
pathDesignsVFinals = "Designs/V_Finals"
pathScriptsVFinals = "Scripts/V_Finals"

# Path to sandbox Final dir
pathSandboxHTMLVFinals = "Sandbox_html_css/assets/pages/vFinals"
pathSandboxNextJsComponentsVFinals = "Sandbox_nextjs/ui/components/vFinals"
pathSandboxNextJsDesignsVFinals = "Sandbox_nextjs/ui/design/vFinals"
pathSandboxPythonVFinals = "Sandbox_python/scripts_vFinals"

def sync_test_directories():
    """
    Synchronizes test directories between source and sandbox paths by copying missing directories
    """
    # Define source and destination path pairs
    path_mappings = [
        (pathComponentsTests, [pathSandboxHTMLTest, pathSandboxNextJsComponentsTests]),
        (pathDesignsTests, [pathSandboxNextJsDesignsTests]),
        (pathScriptsTests, [pathSandboxPythonTests])
    ]
    
    for source_path, destination_paths in path_mappings:
        # Skip if source path doesn't exist
        if not os.path.exists(source_path):
            print(f"Source path {source_path} does not exist")
            continue
            
        # Get list of directories in source path
        source_dirs = [d for d in os.listdir(source_path) 
                      if os.path.isdir(os.path.join(source_path, d))]
        
        # Process each destination path
        for dest_path in destination_paths:
            # Create destination path if it doesn't exist
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
                
            # Get list of directories in destination path
            dest_dirs = [d for d in os.listdir(dest_path) 
                        if os.path.isdir(os.path.join(dest_path, d))]
            
            # Copy missing directories
            for dir_name in source_dirs:
                if dir_name not in dest_dirs:
                    source_dir = os.path.join(source_path, dir_name)
                    
                    # Special handling for Components/Tests with html_css and react_component subdirectories
                    if source_path == pathComponentsTests:
                        sync_component_subdirectories(source_dir, dir_name, dest_path)
                    else:
                        dest_dir = os.path.join(dest_path, dir_name)
                        print(f"Copying {source_dir} to {dest_dir}")
                        shutil.copytree(source_dir, dest_dir)

def sync_component_subdirectories(source_dir, dir_name, dest_path):
    """
    Handles synchronization of component test directories with html_css and react_component subdirectories
    """
    html_css_path = os.path.join(source_dir, "html_css")
    react_component_path = os.path.join(source_dir, "react_component")
    
    # Check if both subdirectories exist
    if os.path.exists(html_css_path) and os.path.exists(react_component_path):
        # Route html_css to HTML sandbox
        if dest_path == pathSandboxHTMLTest:
            dest_dir = os.path.join(dest_path, dir_name)
            print(f"Copying html_css content from {html_css_path} to {dest_dir}")
            shutil.copytree(html_css_path, dest_dir)
        
        # Route react_component to NextJS sandbox
        elif dest_path == pathSandboxNextJsComponentsTests:
            dest_dir = os.path.join(dest_path, dir_name)
            print(f"Copying react_component content from {react_component_path} to {dest_dir}")
            shutil.copytree(react_component_path, dest_dir)
    else:
        # Fallback: copy entire directory if structure doesn't match expected pattern
        dest_dir = os.path.join(dest_path, dir_name)
        print(f"Copying {source_dir} to {dest_dir}")
        shutil.copytree(source_dir, dest_dir)

def sync_vfinal_directories():
    """
    Synchronizes vFinal directories between source and sandbox paths by copying missing directories
    """
    # Define source and destination path pairs
    path_mappings = [
        (pathComponentsVFinals, [pathSandboxHTMLVFinals, pathSandboxNextJsComponentsVFinals]),
        (pathDesignsVFinals, [pathSandboxNextJsDesignsVFinals]),
        (pathScriptsVFinals, [pathSandboxPythonVFinals])
    ]
    
    for source_path, destination_paths in path_mappings:
        # Skip if source path doesn't exist
        if not os.path.exists(source_path):
            print(f"Source path {source_path} does not exist")
            continue
            
        # Get list of directories in source path
        source_dirs = [d for d in os.listdir(source_path) 
                      if os.path.isdir(os.path.join(source_path, d))]
        
        # Process each destination path
        for dest_path in destination_paths:
            # Create destination path if it doesn't exist
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
                
            # Get list of directories in destination path
            dest_dirs = [d for d in os.listdir(dest_path) 
                        if os.path.isdir(os.path.join(dest_path, d))]
            
            # Copy missing directories
            for dir_name in source_dirs:
                if dir_name not in dest_dirs:
                    source_dir = os.path.join(source_path, dir_name)
                    
                    # Special handling for Components/V_Finals with html_css and react_component subdirectories
                    if source_path == pathComponentsVFinals:
                        sync_vfinal_component_subdirectories(source_dir, dir_name, dest_path)
                    else:
                        dest_dir = os.path.join(dest_path, dir_name)
                        print(f"Copying {source_dir} to {dest_dir}")
                        shutil.copytree(source_dir, dest_dir)

def sync_vfinal_component_subdirectories(source_dir, dir_name, dest_path):
    """
    Handles synchronization of component vFinal directories with html_css and react_component subdirectories
    """
    html_css_path = os.path.join(source_dir, "html_css")
    react_component_path = os.path.join(source_dir, "react_component")
    
    # Check if both subdirectories exist
    if os.path.exists(html_css_path) and os.path.exists(react_component_path):
        # Route html_css to HTML sandbox
        if dest_path == pathSandboxHTMLVFinals:
            dest_dir = os.path.join(dest_path, dir_name)
            print(f"Copying html_css content from {html_css_path} to {dest_dir}")
            shutil.copytree(html_css_path, dest_dir)
        
        # Route react_component to NextJS sandbox
        elif dest_path == pathSandboxNextJsComponentsVFinals:
            dest_dir = os.path.join(dest_path, dir_name)
            print(f"Copying react_component content from {react_component_path} to {dest_dir}")
            shutil.copytree(react_component_path, dest_dir)
    else:
        # Fallback: copy entire directory if structure doesn't match expected pattern
        dest_dir = os.path.join(dest_path, dir_name)
        print(f"Copying {source_dir} to {dest_dir}")
        shutil.copytree(source_dir, dest_dir)


def chooseSynchro() :
  choice = input("1 = Synchro Test Dir / 2 = Synchro vFinals : ")
  if choice == "1":
    sync_test_directories()
  elif choice == "2":
    sync_vfinal_directories
  else:
    print("Invalid choice")

chooseSynchro()