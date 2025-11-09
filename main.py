def analyze_text(text):
    # 统计每个字符的出现次数
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    # 按出现频率降序排序
    sorted_chars = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    # 输出结果
    for char, count in sorted_chars:
        print(f"字符 '{char}' 出现 {count} 次")

# 调用示例
if __name__ == "__main__":
    input_text = input("请输入要分析的字符串：")
    analyze_text(input_text)
