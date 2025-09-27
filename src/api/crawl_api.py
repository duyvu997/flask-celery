from flask import Blueprint, request, jsonify
from src.services.celery_worker import celery_app

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
    responses:
      200:
        description: Task started
        schema:
          type: object
          properties:
            task_id:
              type: string
            status:
              type: string
      400:
        description: site_url is required
    """
    data = request.get_json()
    site_url = data.get('site_url')
    if not site_url:
        return jsonify({'error': 'site_url is required'}), 400
    task = celery_app.send_task('crawler.crawl_site', args=[site_url])
    return jsonify({'task_id': task.id, 'status': 'started'})

@crawl_api.route('/crawl/<task_id>', methods=['GET'])
def crawl_status(task_id):
    """
    Get crawl task status/result
    ---
    tags:
      - Crawl
    parameters:
      - in: path
        name: task_id
        required: true
        type: string
    responses:
      200:
        description: Task status/result
        schema:
          type: object
          properties:
            task_id:
              type: string
            status:
              type: string
            result:
              type: string
    """
    result = celery_app.AsyncResult(task_id)
    return jsonify({
        'task_id': task_id,
        'status': result.status,
        'result': result.result if result.successful() else None
    })
