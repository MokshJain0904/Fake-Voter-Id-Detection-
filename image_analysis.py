import cv2
import numpy as np

def preprocess_image(image_path):
    """
    Returns preprocessed grayscale image
    """
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Noise removal
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Adaptive threshold (good for OCR)
    thresh = cv2.adaptiveThreshold(
        blur, 255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11, 2
    )

    return gray, thresh


def blur_detection(gray_image):
    """
    Variance of Laplacian method
    Lower value = more blur
    """
    laplacian_var = cv2.Laplacian(gray_image, cv2.CV_64F).var()
    return laplacian_var


def edge_tampering_score(gray_image):
    """
    Edge inconsistency detection using Canny
    """
    edges = cv2.Canny(gray_image, 50, 150)
    edge_density = np.sum(edges > 0) / edges.size
    return edge_density


def analyze_image(image_path):
    gray, thresh = preprocess_image(image_path)

    blur_score = blur_detection(gray)
    edge_score = edge_tampering_score(gray)

    analysis = {
        "blur_score": round(blur_score, 2),
        "edge_score": round(edge_score, 4)
    }

    return analysis, thresh
