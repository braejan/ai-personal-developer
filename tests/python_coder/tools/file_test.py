import os
import pytest
import tempfile
import sys
from pathlib import Path

# Add the project root to the Python path to make imports work
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.python_coder.tools.files import validate_path, create_new_file


class TestValidatePath:
    def test_not_existing_file(self):
        """Test validate_path with a non-existing file in the current directory."""
        # Create a path to a non-existing file
        non_existing_file = os.path.join(os.path.dirname(__file__), "non_existing_file.txt")
        
        # Make sure the file doesn't exist
        if os.path.exists(non_existing_file):
            os.remove(non_existing_file)
            
        # Test that validate_path raises ValueError for non-existing file
        with pytest.raises(ValueError) as excinfo:
            validate_path(non_existing_file)
        
        # Verify the error message
        assert f"Path {non_existing_file} does not exist." in str(excinfo.value)
    
    def test_not_writable_file(self):
        """Test validate_path with a non-writable file."""
        # Path to the not writable file
        not_writable_file = "/home/braejan/workspace/liwaisi/ai-personal-developer/tests/python_coder/tools/not_writable_file.md"
        
        # Ensure the file exists
        if not os.path.exists(not_writable_file):
            with open(not_writable_file, 'w') as f:
                f.write("This is a test file that will be made non-writable.")
        
        # Make the file non-writable
        current_mode = os.stat(not_writable_file).st_mode
        os.chmod(not_writable_file, current_mode & ~0o222)  # Remove write permissions
        
        try:
            # Test that validate_path raises ValueError for non-writable file
            with pytest.raises(ValueError) as excinfo:
                validate_path(not_writable_file)
            
            # Verify the error message
            assert f"Path {not_writable_file} is not writable." in str(excinfo.value)
        finally:
            # Restore write permissions after test
            os.chmod(not_writable_file, current_mode)
    
    def test_writable_file(self):
        """Test validate_path with a writable file."""
        # Use the current test file as a writable file
        writable_file = __file__
        
        # Ensure the file is writable
        assert os.access(writable_file, os.W_OK), f"Test setup failed: {writable_file} is not writable"
        
        # Test that validate_path returns the path for a writable file
        result = validate_path(writable_file)
        
        # Verify the result is the same as the input path
        assert result == writable_file
    
    def test_create_new_file_already_exists(self):
        """Test create_new_file with a file that already exists."""
        # Path to an existing file
        existing_file = os.path.join(os.path.dirname(__file__), "not_writable_file.md")
        
        # Ensure the file exists
        assert os.path.exists(existing_file), f"Test setup failed: {existing_file} does not exist"
        
        # Test that create_new_file raises ValueError for existing file
        with pytest.raises(ValueError) as excinfo:
            create_new_file(existing_file, "Some content")
        
        # Verify the error message
        assert f"Path {existing_file} already exists." in str(excinfo.value)
    
    def test_create_new_file_success(self):
        """Test create_new_file with a new file."""
        # Path to a new file
        new_file = os.path.join(os.path.dirname(__file__), "_writable_file.md")
        test_content = "# Hello from tests"
        
        # Make sure the file doesn't exist before the test
        if os.path.exists(new_file):
            os.remove(new_file)
        
        try:
            # Test that create_new_file creates the file and returns the path
            result = create_new_file(new_file, test_content)
            
            # Verify the result is the same as the input path
            assert result == new_file
            
            # Verify the file exists
            assert os.path.exists(new_file)
            
            # Verify the content of the file
            with open(new_file, 'r') as f:
                content = f.read()
            assert content == test_content
        finally:
            # Clean up - delete the file after the test
            if os.path.exists(new_file):
                os.remove(new_file)
