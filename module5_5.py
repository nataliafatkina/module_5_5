from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title: str, duration: float | int, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and hash(password) == user.password:
                self.current_user = user
                return f'Здравствуйте, {nickname}. Вход выполнен'
        else:
            return 'Вы ввели неверный пароль'

    def register(self, nickname, password, age):
        user_names = []
        for user in self.users:
            user_names.append(user.nickname)
        if nickname not in user_names:
            user = User(nickname, password, age)
            self.users.append(user)
            self.log_in(nickname, password)
            return f'{nickname}, поздравляем с регистрацией. Вход выполнен'
        else:
            return f'Пользователь {nickname} уже существует'

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        title_video = []
        for video in self.videos:
            title_video.append(video.title)
        for video in args:
            if video.title not in title_video:
                self.videos.append(video)

    def get_videos(self, search_word: str):
        found_videos = []
        selected_videos = []
        for video in self.videos:
            found_videos.append(video.title)
        for video in found_videos:
            if search_word.lower() in video.lower():
                selected_videos.append(video)
        return selected_videos

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for video in self.videos:
                if title == video.title:
                    if self.current_user.age < 18 and video.adult_mode == True:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        sec = 0
                        while sec <= video.duration:
                            print(sec)
                            sleep(1)
                            sec += 1
                            if sec == (video.duration + 1):
                                sec = 0
                                print('Конец видео')
                                break


ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

print('=== Регистрация ===')
# print(ur.current_user)
print(ur.register('vasya_pupkin', 'lolkekcheburek', 13))
# print(ur.current_user)
print(ur.register('vasya_pupkin', 'lheburek', 19))

print()
print('=== Вход по паролю ===')
print(ur.log_in('vasya_pupkin', 'lolkekceburek'))
print(ur.log_in('vasya_pupkin', 'lolkekcheburek'))
# print(ur.users)

print()
print('=== Метод add ===')
ur.add(v1, v2)
print(ur.videos)

v3 = Video('Лучший язык программирования 2024 года', 8)
v4 = Video('Ты мой герой', 120)

ur.add(v3, v4)
print(ur.videos)

print()
print('=== Метод get_videos ===')
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
print(ur.get_videos('ГеР'))

print()
print('=== Метод watch_videos ===')
ur.log_out()
ur.watch_video('Для чего девушкам парень программист?')
ur.log_in('vasya_pupkin', 'lolkekcheburek')
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
ur.watch_video('Лучший язык программирования 2024 года!')
