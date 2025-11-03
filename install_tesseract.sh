#!/usr/bin/env bash
set -o errexit  # 에러 발생 시 중단

# 시스템 패키지 업데이트
apt-get update

# Tesseract 및 한국어 데이터 설치
apt-get install -y tesseract-ocr tesseract-ocr-kor

# 설치 확인 로그
echo "✅ Tesseract installed successfully!"
which tesseract
tesseract --version
