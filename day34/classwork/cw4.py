# 3) N1 დავალებაში შექმნილ tuple-ში შეანაცვლე რომელიმე ელემენტი

sports = ('judo', 'football', 'box', 'MMA', 'volleyball')
sports_list = list(sports)
sports_list[-1] = "Swimming"
sports = tuple(sports_list)

print(sports)