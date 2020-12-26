import cv2
rgb_image = cv2.imread("girls.jpeg")

def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def cropped_image(image):
    cropped = image[10:500, 500:2000]
    viewImage(cropped, "Cropped")

def scale_image(image):
    scale_percent = 20 # Процент от изначального размера
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    viewImage(resized, "Scale 20%")

def rotate_image(image):
    (h, w, d) = image.shape
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, 180, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    viewImage(rotated, "Rotate 180")

def grayscale_image(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, threshold_image = cv2.threshold(image, 127, 255, 0)
    viewImage(gray_image, "Grayscale")
    viewImage(threshold_image, "Threshold")

def blur_image(image):
    blurred = cv2.GaussianBlur(image, (51, 51), 0)
    viewImage(blurred, "Blur")

def rectangle_image(image):
    output = image.copy()
    cv2.rectangle(output, (100, 100), (500, 500), (0, 255, 255), 3)
    viewImage(output, "Rectangle")

def line_image(image):
    output = image.copy()
    cv2.line(output, (60, 20), (400, 200), (0, 255, 0), 3)
    viewImage(output, "Line")

def text_image(image):
    output = image.copy()
    cv2.putText(output, "The best wallpaper", (50, 350),cv2.FONT_HERSHEY_SIMPLEX, 2, (30, 105, 210), 10)
    viewImage(output, "Text")

def face_detected(image_path):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor= 1.1,
        minNeighbors= 5,
        minSize=(10, 10)
    )
    faces_detected = "Face detected: " + format(len(faces))
    print(faces_detected)
    # Рисуем квадраты вокруг лиц
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 255, 0), 2)
    viewImage(image, faces_detected)

def save_image(image_name, image):
    # image = cv2.imread("wallpaper.jpg")
    cv2.imwrite(image_name, image)


if __name__ == '__main__':
    cropped_image(rgb_image)
    scale_image(rgb_image)
    rotate_image(rgb_image)
    grayscale_image(rgb_image)
    blur_image(rgb_image)
    rectangle_image(rgb_image)
    line_image(rgb_image)
    text_image(rgb_image)
    face_detected("girls.jpeg")
    save_image("wallpaper_new.jpg", rgb_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()