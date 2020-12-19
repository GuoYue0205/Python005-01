class InterConverter:
    regex = '[0-9]{4}'
    # to_python to_url 固定格式
    def to_python(self, value):
        return int(value)
    
    def to_url(self, value):
        # return '%04d' % value
        return str(value)
