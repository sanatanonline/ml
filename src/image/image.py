from skimage.metrics import structural_similarity
import cv2


# Works well with images of different dimensions
def orb_sim(img_1, img_2):
    orb = cv2.ORB_create()

    # detect keypoints and descriptors
    kp_a, desc_a = orb.detectAndCompute(img_1, None)
    kp_b, desc_b = orb.detectAndCompute(img_2, None)

    # define the bruteforce matcher object
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # perform matches.
    matches = bf.match(desc_a, desc_b)

    # Look for similar regions with distance < 50. Goes from 0 to 100 so pick a number between.
    similar_regions = [i for i in matches if i.distance < 50]
    if len(matches) == 0:
        return 0
    return len(similar_regions) / len(matches)


# Needs images with same dimension
def structural_sim(img_1, img_2):
    sim, diff = structural_similarity(img_1, img_2, full=True)
    return sim


img1 = cv2.imread('data/img1.png', 0)
img2 = cv2.imread('data/img2.png', 0)

orb_similarity = orb_sim(img1, img2)  # 1.0 means identical. Lower = not similar

print("Similarity using ORB is: ", orb_similarity)

ssim = structural_sim(img1, img2)  # 1.0 means identical. Lower = not similar
print("Similarity using SSIM is: ", ssim)
