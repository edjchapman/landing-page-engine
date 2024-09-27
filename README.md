# Landing Page Engine with Django, React.js, and TinyMCE

[GitHub: CFE Landing Page Engine](https://github.com/codingforentrepreneurs/landing-page-engine-django-react-tinymce)

Student bonus from TinyMCE [https://kirr.co/uhvya9](https://kirr.co/uhvya9).

## Setup Environment Variables

Create an account on:

- [Tiny Cloud](https://kirr.co/xvnpsj)
- [OpenAI](https://openai.com)

Create API Keys at:

- [My Account on Tiny](https://kirr.co/okifco)
- [OpenAI API Keys](https://platform.openai.com/api-keys)

Create `.env`:

```bash
cd ~/dev/landing-page-engine
echo "" >> .env
```

Save API Keys to `.env` with:

```bash
DEBUG=true
SECRET_KEY=your-django-secret
TINY_API_KEY=your-tiny-cloud-api-key
OPENAI_API_KEY=your-openai-api-key
```

(View `.env.sample` if you need a reference)

## Setup Python-Django Backend

```
# mac/linux
python3.12 -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt
```

## Setup ReactJS Frontend

```
npm install
npm run dev
```
