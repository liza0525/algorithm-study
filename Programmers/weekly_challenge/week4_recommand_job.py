def solution(tables, languages, preferences):
    def get_score(priority_language_dict):
        total_score = 0
        for language, score in candidate_dict.items():
            if language in priority_language_dict:
                total_score += score * priority_language_dict[language]

        return total_score

    candidate_dict = {
        language: preference
        for language, preference in zip(languages, preferences)
    }

    score_dict = {}
    for table in tables:
        priority_language_list = table.split()
        job = priority_language_list.pop(0)
        priority_language_dict = {
            priority_language: 5 - i
            for i, priority_language in enumerate(priority_language_list)
        }
        score_dict[job] = get_score(priority_language_dict)

    score_list = sorted(score_dict.items(), key=lambda x: (-x[1], x[0]))
    return max(score_list, key=lambda x: x[1])[0]


# "HARDWARE"
print(solution(
    [
        "SI JAVA JAVASCRIPT SQL PYTHON C#",
        "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
        "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
        "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
        "GAME C++ C# JAVASCRIPT C JAVA"
    ],
    ["PYTHON", "C++", "SQL"],
    [7, 5, 5]
))

# "PORTAL"
print(solution(
    [
        "SI JAVA JAVASCRIPT SQL PYTHON C#",
        "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
        "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
        "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
        "GAME C++ C# JAVASCRIPT C JAVA"
    ],
    ["JAVA", "JAVASCRIPT"],
    [7, 5]
))
