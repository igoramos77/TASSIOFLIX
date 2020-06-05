class Video:
    def __init__(self, id, title, sub_title, category, classification, description, video_url, tumbnail_video, tumbnail_video2, data_create, like, view):
        self._id = id
        self._title = title
        self._sub_title = sub_title
        self._categoty = category
        self._classification = classification
        self._description = description
        self._video_url = video_url
        self._tumbnail_video = tumbnail_video
        self._tumbnail_video2 = tumbnail_video2
        self._data_create = data_create
        self._view = view
        self._like = like

    def getId(self):
        return self._id

    def getTitle(self):
        return self._title

    def getSubTitle(self):
        return self._sub_title

    def getCategory(self):
        return self._categoty

    def getClassification(self):
        return self._classification

    def getDescription(self):
        return self._description

    def setLike(self, like):
        self._like = like
        
    def getLikes(self):
        return self._like

    def getViews(self):
        return self._view

    def setViews(self, view):
        self._view = view

    def getTumbnailVideo(self):
        return self._tumbnail_video

    def getTumbnailVideo2(self):
        return self._tumbnail_video2

    def getVideoUrl(self):
        return self._video_url

    def getDataCreate(self):
        self
        return self._data_create

        