# Python イメージを使用
FROM python:3.10-slim

# 作業ディレクトリ
WORKDIR /app

# ホストユーザーと同じ UID/GID のユーザーを作成
RUN groupadd -g 1000 appuser && \
    useradd -m -u 1000 -g appuser appuser

# 必要なパッケージをインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ユーザーを切り替え
USER appuser

# アプリケーションコードをコピー
COPY . .

# ポートを公開
EXPOSE 8000

# サーバーを起動
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
