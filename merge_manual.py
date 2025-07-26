#!/usr/bin/python3

import os
import re

BASE_DIR = "."
OUTPUT_FILE = "hamonikr_8_manual.txt"

def clean_content_for_ai(content):
    """AI가 읽기 쉽도록 링크와 이미지를 정리"""
    
    # 1. GitBook 전용 문법 제거
    content = re.sub(r'{%\s*content-ref\s+url="[^"]*"\s*%}', '', content)
    content = re.sub(r'{%\s*endcontent-ref\s*%}', '', content)
    content = re.sub(r'{%.*?%}', '', content)  # 기타 GitBook 태그들
    
    # 2. HTML figure 태그와 이미지 제거
    content = re.sub(r'<figure>.*?</figure>', '', content, flags=re.DOTALL)
    content = re.sub(r'<img.*?>', '', content)
    content = re.sub(r'<figcaption>.*?</figcaption>', '', content)
    
    # 3. 마크다운 이미지 제거 (![alt](url) 형태)
    content = re.sub(r'!\[.*?\]\([^)]*\)', '', content)
    
    # 4. 이미지 관련 잔여물 제거
    content = re.sub(r'\.(png|jpg|jpeg|gif|webp|svg)>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'\.(png|jpg|jpeg|gif|webp|svg)\s*alt=.*?>', '', content, flags=re.IGNORECASE)
    content = re.sub(r'src="[^"]*\.(png|jpg|jpeg|gif|webp|svg)[^"]*"', '', content, flags=re.IGNORECASE)
    
    # 5. 내부 링크는 텍스트만 남기기 ([텍스트](파일.md) -> 텍스트)
    content = re.sub(r'\[([^\]]+)\]\([^)]*\.md[^)]*\)', r'\1', content)
    
    # 6. 외부 링크는 "텍스트 (URL)" 형태로 변경
    content = re.sub(r'\[([^\]]+)\]\((https?://[^)]+)\)', r'\1 (\2)', content)
    
    # 7. HTML 앵커 태그 제거
    content = re.sub(r'<a[^>]*href="[^"]*"[^>]*>', '', content)
    content = re.sub(r'</a>', '', content)
    content = re.sub(r'<a[^>]*id="[^"]*"[^>]*>', '', content)
    
    # 8. 기타 HTML 태그 제거
    content = re.sub(r'<mark[^>]*>', '', content)
    content = re.sub(r'</mark>', '', content)
    content = re.sub(r'</?strong>', '', content)
    content = re.sub(r'</?em>', '', content)
    content = re.sub(r'</?code>', '', content)
    
    # 9. 추가 HTML 태그들 제거
    content = re.sub(r'</?div[^>]*>', '', content)
    content = re.sub(r'</?span[^>]*>', '', content)
    content = re.sub(r'</?p[^>]*>', '', content)
    
    # 10. 빈 괄호나 불완전한 태그 제거
    content = re.sub(r'\(\s*\)', '', content)
    content = re.sub(r'<[^>]*>', '', content)  # 남은 모든 HTML 태그
    
    # 11. 이상한 괄호 패턴 정리
    # 파일명이나 단어가 괄호와 이상하게 붙어있는 경우 정리
    content = re.sub(r'([a-zA-Z0-9]+)\)([a-zA-Z0-9]+)', r'\1 \2', content)  # word)word -> word word
    content = re.sub(r'([a-zA-Z0-9]+\.[a-zA-Z0-9]+)\)([a-zA-Z0-9]+)', r'\1 \2', content)  # file.ext)word -> file.ext word
    content = re.sub(r'([a-zA-Z0-9]+)\)\)', r'\1', content)  # word)) -> word
    content = re.sub(r'([a-zA-Z0-9]+)\)\s*\)', r'\1', content)  # word) ) -> word
    
    # 더 복잡한 패턴들 정리
    content = re.sub(r'\.mp4([a-zA-Z0-9]+)\.mp4\)', '.mp4', content)  # .mp4something.mp4) -> .mp4
    content = re.sub(r'([a-zA-Z]+)([a-zA-Z]+)of([a-zA-Z])([a-zA-Z]+)\)', r'\1\2 of \3\4', content)  # wordofword) -> word of word

    # 마크다운 줄바꿈 문법 정리
    content = re.sub(r'\\\s*$', '', content, flags=re.MULTILINE)  # 줄 끝의 백슬래시 제거
    content = re.sub(r'\\\s*\n', '\n', content)  # 백슬래시 + 줄바꿈을 일반 줄바꿈으로

    # 기타 마크다운 문법 정리
    content = re.sub(r'^\s*\\\s*$', '', content, flags=re.MULTILINE)  # 백슬래시만 있는 줄 제거
    
    # 12. 고아 괄호들과 불완전한 줄 제거
    content = re.sub(r'^\s*\)\s*$', '', content, flags=re.MULTILINE)  # 줄 전체가 )만 있는 경우
    content = re.sub(r'^\s*\(\s*$', '', content, flags=re.MULTILINE)  # 줄 전체가 (만 있는 경우
    content = re.sub(r'^\s*\]\s*$', '', content, flags=re.MULTILINE)  # 줄 전체가 ]만 있는 경우
    content = re.sub(r'^\s*\[\s*$', '', content, flags=re.MULTILINE)  # 줄 전체가 [만 있는 경우
    content = re.sub(r'^\s*>\s*$', '', content, flags=re.MULTILINE)   # 줄 전체가 >만 있는 경우
    
    # 13. 연속된 빈 줄 정리
    content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
    
    # 14. HTML 엔티티 디코딩
    content = content.replace('&#x20;', ' ')
    content = content.replace('&amp;', '&')
    content = content.replace('&lt;', '<')
    content = content.replace('&gt;', '>')
    content = content.replace('&nbsp;', ' ')
    content = content.replace('&quot;', '"')
    
    # 15. 불필요한 공백 정리
    content = re.sub(r' +', ' ', content)  # 연속된 공백을 하나로
    content = re.sub(r'\n +', '\n', content)  # 줄 시작의 공백 제거
    content = re.sub(r' +\n', '\n', content)  # 줄 끝의 공백 제거
    
    # 16. 다시 한번 연속된 빈 줄 정리 (고아 괄호 제거 후)
    content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
    
    return content.strip()

def process_md_file(filepath, md_content):
    """마크다운 파일을 처리하여 AI 친화적인 텍스트로 변환"""
    # 내용 정리
    cleaned_content = clean_content_for_ai(md_content)
    
    # 파일 간 구분을 위한 공백 추가
    processed_content = cleaned_content + "\n\n---\n\n"
    
    return processed_content

merged_text = "# 하모니카 8.0 통합 매뉴얼\n\n"
merged_text += "\n\n"

file_count = 0
for root, _, files in os.walk(BASE_DIR):
    for file in sorted(files):
        if file.endswith(".md"):
            # license.md 파일은 제외
            if file == "license.md":
                continue
                
            filepath = os.path.join(root, file)
            try:
                with open(filepath, "r", encoding="utf-8") as f:
                    md_content = f.read()
                processed_content = process_md_file(filepath, md_content)
                merged_text += processed_content
                file_count += 1
            except Exception as e:
                print(f"⚠️ 오류 발생: {filepath} - {e}")

# 마지막 구분자 제거
merged_text = merged_text.rstrip("\n---\n\n") + "\n"

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(merged_text)

print(f"✅ 병합 완료: {OUTPUT_FILE}")
print(f"📊 처리된 파일 수: {file_count}개")

