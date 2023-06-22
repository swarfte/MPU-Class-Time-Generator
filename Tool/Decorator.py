import datetime as dt
import functools

keywords = {
    "default": "decorated function name"
}


class AbstractDecorator(object):  # 裝飾函數的裝飾器
    """ Basic decorators are used to extend other functions  """

    def __init__(self, *args, **kwargs):  # 獲取裝飾器初始化的傳入參數
        super(AbstractDecorator, self).__init__()
        self.func = None  # 被裝飾的函數
        self.func_args = None  # 被裝飾函數的可變位置參數
        self.func_kwargs = None  # 被裝飾函數的關鍵字參數
        self.func_result = None  # 被裝飾函數運行後的返回值
        self.decorator_args = args  # 對像裝飾器自身的可變位置參數
        self.decorator_kwargs = kwargs  # 對像裝飾器自身的關鍵字參數

    def __call__(self, func):  # class被當作函數調用時接收的參數(接收一個function作為參數->裝飾器)
        self.func = func
        return self.run(self.func)

    def run(self, func):  # 運行裝飾器函數
        """Run the decorator function"""

        @functools.wraps(func)  # 保留被裝飾函數的屬性
        def wrapper(*args, **kwargs):  # 對被裝飾函數修改/增加額外的功能
            """the decorator main control function """
            self.initialize(args, kwargs)
            self.before_invoke()
            self.invoke()
            self.after_invoke()
            return self.func_result

        return wrapper

    def initialize(self, args, kwargs):  # 裝飾器函數運行前的初始化工作
        """Initialization work before the decorator function runs"""
        self.func_args = args
        self.func_kwargs = kwargs

    def before_invoke(self):  # 被裝飾函數運行前的工作
        """Work before the decorated function runs"""
        pass

    def invoke(self):  # 調用被裝飾的函數
        """Call the decorated function """
        self.func_result = self.func(*self.func_args, **self.func_kwargs)

    def after_invoke(self):  # 被裝飾函數運行後的工作 (在被裝飾的函數return 前執行)
        """Work after the decorated function runs"""
        pass


class RunTimeMonitor(AbstractDecorator):  # 記錄被裝飾函數的運行時間
    """Record the running time of the decorated function"""

    def __init__(self, sentence: str = keywords["default"]):
        super(RunTimeMonitor, self).__init__()
        self.sentence = str(sentence)  # 要表達函式
        self.start_time = None  # 開始運行的時間
        self.end_time = None  # 結束運行的時間
        self.run_time = 0  # 記錄被裝飾函數運行的時間

    def start_count_time(self):  # 調用被裝飾函數並開始計時
        """Call the decorated function and start timing"""
        self.start_time = dt.datetime.now().strftime("%H:%M:%S.%f")
        self.run_time = int(self.start_time[0:2]) * 3600 + int(self.start_time[3:5]) * 60 + int(
            self.start_time[6:8]) + float(self.start_time[9:11]) / 1000

    def show_start_time(self):  # 展示被裝飾函數的開始時間
        """Displays the start time of the decorated function"""
        print(f'[{self.sentence}] start time: {self.start_time}')

    def before_invoke(self):
        self.start_count_time()
        if self.sentence == keywords["default"]:
            self.sentence = self.func.__name__
        self.show_start_time()
