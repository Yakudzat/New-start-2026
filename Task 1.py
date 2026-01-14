import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class RecoveryGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Welcome Back!")
        arcade.set_background_color(arcade.color.BLACK)

        # Списки спрайтов
        self.all_sprites = arcade.SpriteList()

        # Создаем объекты
        self.asteroid = arcade.Sprite(":resources:/images/space_shooter/meteorGrey_big1.png", 0.8)
        self.asteroid.center_x = 0
        self.asteroid.center_y = 0
        self.all_sprites.append(self.asteroid)

        self.star = arcade.Sprite(":resources:images/items/star.png", scale=0.8)
        self.star.center_x = 400
        self.star.center_y = 300
        self.all_sprites.append(self.star)

        self.player = None
        self.space_pressed = False
        self.speed = 4
        self.player_scale_normal = 0.8
        self.player_scale_boosted = 1.6

        # Переменные для анимации
        self.scale_speed = 0.01
        self.asteroid_speed = 1.5
        self.star_scale_step = 0.01

        self.setup()

    def setup(self):
        self.player = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png", 0.8)

        self.player.center_x = SCREEN_WIDTH / 2
        self.player.center_y = SCREEN_HEIGHT / 2
    def on_draw(self):
        self.clear()
        self.all_sprites.draw()

    def on_update(self, delta_time):

        self.player.center_x += self.player.change_x

        self.player.center_y += self.player.change_y

        if self.space_pressed:
            self.player.scale = self.player_scale_boosted
        else:
            self.player.scale = self.player_scale_normal


        self.asteroid.center_x += self.asteroid_speed
        self.asteroid.center_y += self.asteroid_speed

        if self.asteroid.center_x > SCREEN_WIDTH:
            self.asteroid.center_x = 0
        elif self.asteroid.center_x < -SCREEN_WIDTH:
            self.asteroid.center_x = SCREEN_WIDTH

        if self.asteroid.center_y > SCREEN_HEIGHT:
            self.asteroid.center_y = 0



        # 1. Вращение
        self.star.angle += 3

        # 2. Пульсация (допиши логику здесь)
        current_s = self.star.scale[0] + self.star_scale_step
        current_c = self.star.scale[1] + self.star_scale_step
        if current_s > 1.2 or current_s < 0.5:
            self.star_scale_step *= -1

        self.star.scale = (current_s, current_c)
        # ... твой код ...

    def on_key_press(self, key, modifiers):
        # 3. Управление (допиши здесь)
        match key:
            case arcade.key.LEFT:
                self.player.change_x = -self.speed
            case arcade.key.RIGHT:
                self.player.change_x = self.speed
            case arcade.key.DOWN:
                self.player.change_y = -self.speed
            case arcade.key.UP:
                self.player.change_y = self.speed
        arcade.play_sound(arcade.load_sound(":resources:/sounds/rockHit2.wav"), 0.5)

        if key == arcade.key.SPACE:
            self.space_pressed = True



    def on_key_release(self, key, modifiers):
        match key:
            case arcade.key.LEFT | arcade.key.RIGHT:
                self.player.change_x = 0
            case arcade.key.UP | arcade.key.DOWN:
                self.player.change_y = 0

        if key == arcade.key.SPACE:
            self.space_pressed = False

if __name__ == "__main__":
    game = RecoveryGame()
    arcade.run()