# Importing the Required Modules
import cv2 as cv
import os

def create_sketch(image_path, blur_radius=21, save_as_color=False, output_format="png"):
    # Check if the image exists
    if not os.path.exists(image_path):
        print("Error: The image file does not exist.")
        return

    # Reading the image
    image = cv.imread(image_path)

    # Converting the Image into gray_image
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Inverting the Image
    invert_image = cv.bitwise_not(gray_image)

    # Blur Image
    blur_image = cv.GaussianBlur(invert_image, (blur_radius, blur_radius), 0)

    # Inverting the Blurred Image
    invert_blur = cv.bitwise_not(blur_image)

    # Convert Image Into Sketch
    sketch = cv.divide(gray_image, invert_blur, scale=256.0)

    # Displaying the Sketch in real-time
    cv.imshow("Sketch Preview", sketch)
    cv.waitKey(0)  # Wait for a key press
    cv.destroyAllWindows()

    # If save_as_color is True, blend the sketch with the original image
    if save_as_color:
        color_sketch = cv.addWeighted(image, 0.5, cv.cvtColor(sketch, cv.COLOR_GRAY2BGR), 0.5, 0)
        output_image = color_sketch
    else:
        output_image = sketch

    # Saving the Sketch Image
    output_filename = f"Sketch_Output.{output_format}"
    if cv.imwrite(output_filename, output_image):
        print(f"Sketch saved successfully as {output_filename}.")
    else:
        print("Failed to save the sketch.")

# Main Execution
if __name__ == "__main__":
    # Input the image path from the user
    image_path = input("Enter the path to the image: ")

    # Input blur radius from the user
    blur_radius = int(input("Enter blur radius (odd number, e.g., 21): "))

    # Ask if the user wants a color sketch
    save_as_color = input("Do you want a color sketch? (yes/no): ").strip().lower() == "yes"

    # Input the desired output format
    output_format = input("Enter output format (e.g., png, jpg): ").strip().lower()

    # Call the function to create the sketch
    create_sketch(image_path, blur_radius, save_as_color, output_format)
