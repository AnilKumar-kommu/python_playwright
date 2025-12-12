from http.client import responses


from playwright.sync_api import Playwright



def test_headers_respones(playwright:Playwright):
    request_context=playwright.request.new_context()
    response=request_context.get("https://www.google.com")

    assert response.status_text == "OK"
    assert response.status == 200

    headers=response.headers
    for key, value in headers.items():

        assert "text/html" in headers.get("content-type")
        assert "gzip" == headers.get("content-encoding")
        print(f"keay name===>{key}:\n value ===>{value}")
        print(headers.get("content-type"))
