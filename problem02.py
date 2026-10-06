# 높이와 너비를 입력받아 정수로 바꾼다.
size = input().split()
H = int(size[0])
W = int(size[1])

# 이미지 전체의 밝기를 저장한다.
brightness_image = []

# 모든 픽셀의 밝기 합을 저장한다.
total_brightness = 0

# 높이 H만큼 한 행씩 입력받는다.
for row_index in range(H):
    # 공백으로 한 행의 픽셀들을 구분한다.
    pixels = input().split()

    # 현재 행의 밝기를 저장할 리스트를 만든다.
    row_brightness = []

    # 현재 행의 픽셀을 하나씩 처리한다.
    for pixel in pixels:
        # RGB를 쉼표로 나누고 정수로 바꾼다.
        rgb = pixel.split(",")
        R = int(rgb[0])
        G = int(rgb[1])
        B = int(rgb[2])

        # RGB의 평균으로 밝기를 계산한다.
        brightness = (R + G + B) // 3

        # 밝기를 현재 행에 저장하고 전체 합에도 더한다.
        row_brightness.append(brightness)
        total_brightness += brightness

    # 완성된 행을 이미지 전체에 저장한다.
    brightness_image.append(row_brightness)

# 모든 픽셀의 평균 밝기를 임계값으로 정한다.
pixel_count = H * W
threshold = total_brightness // pixel_count

# 첫째 줄에 임계값을 출력한다.
print(threshold)

# 저장된 밝기를 한 행씩 꺼낸다.
for row in brightness_image:
    # 현재 행의 흑백 결과를 저장한다.
    result_row = []

    # 각 픽셀의 밝기를 임계값과 비교한다.
    for brightness in row:
        if brightness >= threshold:
            # 임계값 이상이면 흰색 1을 저장한다.
            result_row.append("1")
        else:
            # 임계값 미만이면 검은색 0을 저장한다.
            result_row.append("0")

    # 한 행의 결과를 공백 없이 연결해서 출력한다.
    print("".join(result_row))