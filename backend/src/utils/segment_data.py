class DataSegmenter:
    def __init__(self, soup):
        self.soup = soup

    def segment_data(self):
        elements = []
        for element in self.soup.find_all(['p', 'h3', 'ul', 'li', 'ol', 'h1', 'h2', 'h4', 'h5', 'h6']):
            if element.name == 'p':
                elements.append(element.text.strip())
            elif element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                elements.append(f"[Title: {element.text.strip()}]")
            elif element.name == 'ul':
                list_items = [li.text.strip() for li in element.find_all('li')]
                elements.append(f"[List: {', '.join(list_items)}]")
            elif element.name == 'ol':
                list_items = [li.text.strip() for li in element.find_all('li')]
                elements.append(f"[Ordered List: {', '.join(list_items)}]")

        segments = []
        current_segment = []

        for element in elements:
            if element.startswith("[Title:"):
                if current_segment:
                    segments.append(current_segment)
                    current_segment = []
            current_segment.append(element)

        if current_segment:
            segments.append(current_segment)

        segments = [segment for segment in segments if any(segment)]
        return segments
