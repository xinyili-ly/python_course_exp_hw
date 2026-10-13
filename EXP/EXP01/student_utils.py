def parse_student(line):
    line = line.strip()
    parts = line.split(",")
    if len(parts) != 2:
        raise ValueError("字段数量错误，必须name,score两个字段")
    name = parts[0].strip()
    score_str = parts[1].strip()
    if len(name) == 0:
        raise ValueError("姓名不能为空")
    try:
        score = int(score_str)
    except ValueError:
        raise ValueError("成绩无法转为整数")
    if not (0 <= score <= 100):
        raise ValueError(f"成绩{score}超出0‑100范围")
    return {"name": name, "score": score}
