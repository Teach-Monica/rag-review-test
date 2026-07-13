from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404
from documents.models import Document

def download_document(request, doc_id):
    doc = get_object_or_404(Document, id=doc_id)
    file_path = doc.file_path
    response = FileResponse(open(file_path, "rb"))
    response["Content-Disposition"] = f'attachment; filename="{doc.filename}"'
    return response

def delete_document(request, doc_id):
    doc = get_object_or_404(Document, id=doc_id)
    doc.delete()
    return JsonResponse({"status": "deleted"})
