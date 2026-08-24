# Markdown -> PDF renderer for the association's documents.
# Pinned base image so a rebuild in two years produces the same typography.
FROM python:3.12-slim-bookworm

# WeasyPrint needs Pango/HarfBuzz for text shaping; the font packages are what
# the documents are actually typeset in, so they are part of the contract.
RUN apt-get update && apt-get install -y --no-install-recommends \
        libpango-1.0-0 \
        libpangoft2-1.0-0 \
        libharfbuzz0b \
        libffi8 \
        fonts-crosextra-caladea \
        fonts-liberation \
        fonts-dejavu-core \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY render.py /opt/pdf/render.py
COPY config.yaml /opt/pdf/config.yaml
COPY style /opt/pdf/style

# The container runs as the invoking user, who has no home directory here;
# fontconfig and matplotlib-style caches must land somewhere writable.
ENV XDG_CACHE_HOME=/tmp/cache \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /work
ENTRYPOINT ["python", "/opt/pdf/render.py"]
