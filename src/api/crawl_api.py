from flask import Blueprint, request, jsonify
from src.lib.crawl_service import CrawlService

crawl_api = Blueprint('crawl_api', __name__)

@crawl_api.route('/crawl', methods=['POST'])
def trigger_crawl():
    """
    Trigger a crawl task
    ---
    tags:
      - Crawl
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            site_url:
              type: string
              example: "https://nettruyen3qb.com/"
            source_key:
              type: string
              example: "nettruyen"
    responses:
      200:
        description: Task started
        schema:
          type: object
          properties:
            info:
              type: object
            chapters:
              type: array
              items:
                type: string
      400:
        description: site_url and source_key are required
    """
    data = request.get_json()
    site_url = data.get('site_url')
    source_key = data.get('source_key')
    if not site_url or not source_key:
        return jsonify({'error': 'site_url and source_key are required'}), 400
    service = CrawlService(source_key)
    result = service.crawl_comic(site_url)
    return jsonify(result)
