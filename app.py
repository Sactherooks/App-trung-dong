import random
import sys
import pygame
 
# ---- Config ----
SCREEN_WIDTH = 1860
SCREEN_HEIGHT = 960
FPS = 60
 
PLAYER_SPEED = 6
JUMP_SPEED = 10
GRAVITY = 0.35
PARRY_DURATION = 250
PARRY_COOLDOWN = 700
 
PROJECTILE_SPEED_START = 2.5
PROJECTILE_ACCELERATION = 0.05
PROJECTILE_SPAWN_TIME = 1100
 
ITEM_SPAWN_TIME = 10000
ITEM_DURATION = 3000
ANIM_FRAME_SPEED = 333
 
# ---- Đường dẫn tài nguyên (chỉnh lại nếu cần) ----
ASSET_PATH = "C:/Users/TBL/Documents/GitHub/App-trung-dong/"
 
# ---- Danh sách nhân vật ----
# Thêm / bớt nhân vật tại đây.
# Mỗi nhân vật cần: name, idle_image, walk_frames, parry_image
# (dùng None nếu ảnh chưa có – game sẽ tự render hình chữ nhật màu)
CHARACTERS = [
    {
        "id": "hero",
        "name": "Nhà Tu Hành",
        "desc": "Chiến binh cân bằng, dễ chơi.",
        "color": (20, 120, 20),          # màu fallback
        "idle":   ASSET_PATH + "mc_normal.png",
        "walk":  [
            ASSET_PATH + "Không Có Tiêu Đề9_20260402131643.png",
            ASSET_PATH + "Không Có Tiêu Đề9_20260402131649.png",
        ],
        "parry":  ASSET_PATH + "Không Có Tiêu Đề51_20260402134240.png",
        "portrait": ASSET_PATH + "mc_normal.png",   # ảnh to trong màn chọn
        "anim_frames": [
            ASSET_PATH + "Không Có Tiêu Đề48_20260402131904.png",
            ASSET_PATH + "Không Có Tiêu Đề48_20260402131946.png",
            ASSET_PATH + "Không Có Tiêu Đề48_20260402131950.png",
            ASSET_PATH + "Không Có Tiêu Đề48_20260402131954.png",
            ASSET_PATH + "Không Có Tiêu Đề48_20260402131958.png",
            ASSET_PATH + "Không Có Tiêu Đề48_20260402132001.png",
            ASSET_PATH + "Không Có Tiêu Đề48_20260402132004.png",
            ASSET_PATH + "Không Có Tiêu Đề48_20260402132007.png",
            ASSET_PATH + "Không Có Tiêu Đề48_20260402132010.png",
        ],
    },
    # nhân vật 2
    {
        "id": "archer",
        "name": "Cung Thủ",
        "desc": "Linh hoạt, tốc độ cao.",
        "color": (20, 60, 160),
        "idle":   ASSET_PATH + "nv2/Đứng.png",
        "walk":  [ASSET_PATH + "nv2/Không Có Tiêu Đề75_20260509092648.png", ASSET_PATH + "nv2/Không Có Tiêu Đề75_20260509092652.png", ASSET_PATH + "nv2/Không Có Tiêu Đề75_20260509092657.png", ASSET_PATH + "nv2/Không Có Tiêu Đề75_20260509092708.png", ASSET_PATH + "nv2/Không Có Tiêu Đề75_20260509092724.png"],
        "parry":  ASSET_PATH + "nv2/Đỡ.png",
        "portrait": ASSET_PATH + "nv2/Đứng.png",
        "anim_frames": [
            ASSET_PATH + "nv2/drive-download-20260512T023001Z-3-001/Không Có Tiêu Đề78_20260509092906.png",
            ASSET_PATH + "nv2/drive-download-20260512T023001Z-3-001/Không Có Tiêu Đề78_20260509092910.png",
            ASSET_PATH + "nv2/drive-download-20260512T023001Z-3-001/Không Có Tiêu Đề78_20260509092913.png",
            ASSET_PATH + "nv2/drive-download-20260512T023001Z-3-001/Không Có Tiêu Đề78_20260509092916.png",
            ASSET_PATH + "nv2/drive-download-20260512T023001Z-3-001/Không Có Tiêu Đề78_20260509092919.png",
            ASSET_PATH + "nv2/drive-download-20260512T023001Z-3-001/Không Có Tiêu Đề78_20260509092923.png",
            ASSET_PATH + "nv2/drive-download-20260512T023001Z-3-001/Không Có Tiêu Đề78_20260509092946.png",
            ASSET_PATH + "nv2/drive-download-20260512T023001Z-3-001/Không Có Tiêu Đề78_20260509092951.png",
            ASSET_PATH + "nv2/drive-download-20260512T023001Z-3-001/Không Có Tiêu Đề78_20260509092955.png",
            ASSET_PATH + "nv2/drive-download-20260512T023001Z-3-001/Không Có Tiêu Đề78_20260509093000.png",
            ASSET_PATH + "nv2/drive-download-20260512T023001Z-3-001/Không Có Tiêu Đề78_20260509093026.png",
            ASSET_PATH + "nv2/drive-download-20260512T023001Z-3-001/Không Có Tiêu Đề78_20260509093030.png",
            ASSET_PATH + "nv2/drive-download-20260512T023001Z-3-001/Không Có Tiêu Đề78_20260509093034.png",
            ASSET_PATH + "nv2/drive-download-20260512T023001Z-3-001/Không Có Tiêu Đề78_20260509093041.png",
            ASSET_PATH + "nv2/drive-download-20260512T023001Z-3-001/Không Có Tiêu Đề78_20260509093049.png",
            ASSET_PATH + "nv2/drive-download-20260512T023001Z-3-001/Không Có Tiêu Đề78_20260509093054.png",
        ]
    },
    # ---- Thêm nhân vật 3 ở đây ----
    # {
    #     "id": "monk",
    #     "name": "Thiền Sư",
    #     "desc": "Parry lâu hơn, di chuyển chậm hơn.",
    #     "color": (160, 80, 10),
    #     "idle":   ASSET_PATH + "monk_idle.png",
    #     "walk":  [ASSET_PATH + "monk_walk1.png", ASSET_PATH + "monk_walk2.png"],
    #     "parry":  ASSET_PATH + "monk_parry.png",
    #     "portrait": ASSET_PATH + "monk_idle.png",
    # },
]
 
 
# ---- Helpers ----
 
def try_load_image(path, size=None):
    try:
        img = pygame.image.load(path).convert_alpha()
        if size:
            img = pygame.transform.scale(img, size)
        return img
    except Exception:
        return None
 
 
def draw_text(surf, text, size, x, y, color=(255, 255, 255), font_name="arial"):
    font = pygame.font.SysFont(font_name, size, bold=True)
    surf.blit(font.render(text, True, color), (x, y))
 
 
def draw_text_centered(surf, text, size, cx, y, color=(255, 255, 255), font_name="arial"):
    font = pygame.font.SysFont(font_name, size, bold=True)
    rendered = font.render(text, True, color)
    surf.blit(rendered, (cx - rendered.get_width() // 2, y))
 
 
def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))
 
 
# ================================================================
#  MÀN HÌNH CHỌN NHÂN VẬT
# ================================================================
 
class CharacterSelectScreen:
    """Hiển thị màn hình chọn nhân vật, trả về index nhân vật được chọn."""
 
    CARD_W = 320
    CARD_H = 480
    CARD_GAP = 60
    PORTRAIT_SIZE = (240, 300)
 
    def __init__(self, screen, bg_image):
        self.screen = screen
        self.bg_image = bg_image
        self.screen_rect = screen.get_rect()
        self.selected = 0          # nhân vật đang được highlight
        self.confirmed = False
        self.clock = pygame.time.Clock()
 
        # Load ảnh chân dung nhân vật
        self.portraits = []
        for ch in CHARACTERS:
            img = try_load_image(ch["portrait"], self.PORTRAIT_SIZE)
            if img is None:
                img = pygame.Surface(self.PORTRAIT_SIZE, pygame.SRCALPHA)
                pygame.draw.rect(img, ch["color"], img.get_rect(), border_radius=16)
            self.portraits.append(img)
 
        # Tạo overlay tối cho các card chưa chọn
        self.dim_overlay = pygame.Surface((self.CARD_W, self.CARD_H), pygame.SRCALPHA)
        self.dim_overlay.fill((0, 0, 0, 140))
 
        # Animation highlight (nhấp nháy viền)
        self.blink_timer = 0
 
        # Particle đơn giản để tạo không khí
        self.particles = [self._new_particle() for _ in range(60)]
 
    # ---- Particle helpers ----
    def _new_particle(self):
        return {
            "x": random.randint(0, self.screen_rect.width),
            "y": random.randint(0, self.screen_rect.height),
            "r": random.uniform(1, 3),
            "speed": random.uniform(0.2, 0.8),
            "alpha": random.randint(60, 180),
        }
 
    def _update_particles(self):
        for p in self.particles:
            p["y"] -= p["speed"]
            if p["y"] < -5:
                p["x"] = random.randint(0, self.screen_rect.width)
                p["y"] = self.screen_rect.height + 5
 
    def _draw_particles(self):
        for p in self.particles:
            s = pygame.Surface((int(p["r"] * 2), int(p["r"] * 2)), pygame.SRCALPHA)
            pygame.draw.circle(s, (255, 220, 120, p["alpha"]), (int(p["r"]), int(p["r"])), int(p["r"]))
            self.screen.blit(s, (int(p["x"] - p["r"]), int(p["y"] - p["r"])))
 
    # ---- Card vị trí ----
    def _card_rects(self):
        total_w = len(CHARACTERS) * self.CARD_W + (len(CHARACTERS) - 1) * self.CARD_GAP
        start_x = self.screen_rect.centerx - total_w // 2
        cy = self.screen_rect.centery - self.CARD_H // 2 + 20
        rects = []
        for i in range(len(CHARACTERS)):
            x = start_x + i * (self.CARD_W + self.CARD_GAP)
            rects.append(pygame.Rect(x, cy, self.CARD_W, self.CARD_H))
        return rects
 
    # ---- Vẽ một card ----
    def _draw_card(self, idx, rect, selected):
        ch = CHARACTERS[idx]
        self.blink_timer += 0
        border_color = (255, 210, 60) if selected else (80, 60, 30)
        border_w = 4 if selected else 2
 
        # Nền card
        card_surf = pygame.Surface((self.CARD_W, self.CARD_H), pygame.SRCALPHA)
        if selected:
            pygame.draw.rect(card_surf, (60, 40, 10, 210), card_surf.get_rect(), border_radius=18)
        else:
            pygame.draw.rect(card_surf, (20, 15, 5, 160), card_surf.get_rect(), border_radius=18)
        self.screen.blit(card_surf, rect)
 
        # Viền
        pygame.draw.rect(self.screen, border_color, rect, border_w, border_radius=18)
 
        # Chân dung
        portrait = self.portraits[idx]
        px = rect.x + (self.CARD_W - self.PORTRAIT_SIZE[0]) // 2
        py = rect.y + 30
        self.screen.blit(portrait, (px, py))
 
        # Tên
        draw_text_centered(self.screen, ch["name"], 30, rect.centerx, py + self.PORTRAIT_SIZE[1] + 16,
                           color=(255, 220, 80) if selected else (200, 180, 120))
 
        # Mô tả
        draw_text_centered(self.screen, ch["desc"], 20, rect.centerx, py + self.PORTRAIT_SIZE[1] + 56,
                           color=(240, 230, 200) if selected else (140, 120, 80))
 
        # Badge "ĐÃ CHỌN"
        if selected:
            badge_y = rect.bottom - 52
            pygame.draw.rect(self.screen, (200, 160, 20), (rect.x + 60, badge_y, self.CARD_W - 120, 36), border_radius=8)
            draw_text_centered(self.screen, "▶  CHỌN NHÂN VẬT NÀY", 18, rect.centerx, badge_y + 9,
                               color=(30, 20, 5))
 
        if not selected:
            self.screen.blit(self.dim_overlay, rect)
 
    # ---- Vòng lặp chính ----
    def run(self):
        """Chạy màn hình chọn nhân vật. Trả về index nhân vật khi người dùng xác nhận."""
        while True:
            dt = self.clock.tick(FPS)
            self.blink_timer += dt
 
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_LEFT, pygame.K_a):
                        self.selected = (self.selected - 1) % len(CHARACTERS)
                    if event.key in (pygame.K_RIGHT, pygame.K_d):
                        self.selected = (self.selected + 1) % len(CHARACTERS)
                    if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        return self.selected
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                # Click chuột vào card
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for i, r in enumerate(self._card_rects()):
                        if r.collidepoint(event.pos):
                            if self.selected == i:
                                return self.selected
                            self.selected = i
 
            # Vẽ nền
            if self.bg_image:
                self.screen.blit(self.bg_image, (0, 0))
            else:
                self.screen.fill((15, 10, 5))
 
            # Lớp tối phủ lên nền cho dễ đọc
            overlay = pygame.Surface((self.screen_rect.width, self.screen_rect.height), pygame.SRCALPHA)
            overlay.fill((0, 0, 0, 120))
            self.screen.blit(overlay, (0, 0))
 
            self._update_particles()
            self._draw_particles()
 
            # Tiêu đề
            draw_text_centered(self.screen, "⚔  CHỌN NHÂN VẬT  ⚔", 52,
                               self.screen_rect.centerx, 60, color=(255, 210, 60))
            draw_text_centered(self.screen, "← → để chuyển   •   ENTER hoặc Click để xác nhận",
                               22, self.screen_rect.centerx, 128, color=(200, 180, 130))
 
            # Các card nhân vật
            for i, rect in enumerate(self._card_rects()):
                self._draw_card(i, rect, i == self.selected)
 
            # Hướng dẫn phím dưới cùng
            draw_text_centered(self.screen, "ESC – Thoát", 20,
                               self.screen_rect.centerx, self.screen_rect.bottom - 40,
                               color=(120, 100, 70))
 
            pygame.display.flip()
 
 
# ================================================================
#  PLAYER (nhận thêm tham số char_data)
# ================================================================
 
class Player:
    def __init__(self, screen_rect, char_data):
        self.width = 250
        self.height = 250
 
        self.rect = pygame.Rect(
            screen_rect.centerx - self.width // 2,
            screen_rect.bottom - self.height - 120,
            self.width,
            self.height,
        )
        self.speed = PLAYER_SPEED
        self.vy = 0
        self.on_ground = True
        self.ground_y = self.rect.y
 
        self.parry_active = False
        self.parry_timer = 0
        self.parry_cooldown = 0
 
        # Load ảnh theo char_data
        fallback = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        pygame.draw.rect(fallback, char_data.get("color", (20, 120, 20)),
                         (0, 0, self.width, self.height), border_radius=10)
 
        self.image_idle = try_load_image(char_data["idle"], (self.width, self.height)) or fallback
        self.frames = []
        for path in char_data.get("walk", []):
            img = try_load_image(path, (self.width, self.height))
            self.frames.append(img if img else fallback)
        if not self.frames:
            self.frames = [fallback]
 
        self.image_parry = try_load_image(char_data["parry"], (self.width, self.height)) or fallback
 
        self.image = self.image_idle
        self.anim_index = 0
        self.anim_timer = 0
        self.anim_speed = 150
 
    def update(self, keys, screen_rect, dt):
        dx = 0
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += self.speed
 
        self.rect.x += dx
        self.rect.x = max(screen_rect.left, min(self.rect.x, screen_rect.right - self.rect.width))
 
        if (keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:
            self.vy = -JUMP_SPEED
            self.on_ground = False
 
        self.vy += GRAVITY
        self.rect.y += self.vy
 
        if self.rect.y >= self.ground_y:
            self.rect.y = self.ground_y
            self.vy = 0
            self.on_ground = True
        else:
            self.on_ground = False
 
        if self.parry_cooldown > 0:
            self.parry_cooldown = max(0, self.parry_cooldown - dt)
        if self.parry_active:
            self.parry_timer = max(0, self.parry_timer - dt)
            if self.parry_timer <= 0:
                self.parry_active = False
 
        if keys[pygame.K_f] and self.parry_cooldown <= 0 and not self.parry_active:
            self.parry_active = True
            self.parry_timer = PARRY_DURATION
            self.parry_cooldown = PARRY_COOLDOWN
 
        is_moving = keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_RIGHT] or keys[pygame.K_d]
 
        if self.parry_active:
            self.image = self.image_parry
        elif is_moving:
            self.anim_timer += dt
            if self.anim_timer >= self.anim_speed:
                self.anim_timer = 0
                self.anim_index = (self.anim_index + 1) % len(self.frames)
            self.image = self.frames[self.anim_index]
        else:
            self.anim_index = 0
            self.anim_timer = 0
            self.image = self.image_idle
 
    def draw(self, surf):
        if self.parry_active:
            glow = pygame.Surface((self.width + 14, self.height + 14), pygame.SRCALPHA)
            pygame.draw.ellipse(glow, (120, 200, 255, 140), glow.get_rect())
            surf.blit(glow, (self.rect.x - 7, self.rect.y - 7))
        surf.blit(self.image, self.rect)
 
 
# ================================================================
#  PROJECTILE, ITEM (không thay đổi)
# ================================================================
 
class Projectile:
    def __init__(self, screen_rect, speed):
        self.width = 150
        self.height = 150
        self.speed = speed
 
        self.direction = random.choices(
            ["top", "left", "right", "bottom"],
            weights=[80, 8, 8, 4],
            k=1,
        )[0]
 
        if self.direction == "top":
            self.x = random.randint(screen_rect.left + 16, screen_rect.right - 16 - self.width)
            self.y = screen_rect.top - self.height - 10
            self.vx = 0
            self.vy = self.speed
            self.angle = 0
        elif self.direction == "bottom":
            self.x = random.randint(screen_rect.left + 16, screen_rect.right - 16 - self.width)
            self.y = screen_rect.bottom + 10
            self.vx = 0
            self.vy = -self.speed
            self.angle = 180
        elif self.direction == "left":
            self.x = screen_rect.left - self.width - 10
            self.y = random.randint(screen_rect.top + 16, screen_rect.bottom - 16 - self.height)
            self.vx = self.speed
            self.vy = 0
            self.angle = 90
        else:
            self.x = screen_rect.right + 10
            self.y = random.randint(screen_rect.top + 16, screen_rect.bottom - 16 - self.height)
            self.vx = -self.speed
            self.vy = 0
            self.angle = 270
 
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.entered = False
 
        self.image = try_load_image(ASSET_PATH + "Fiery katana with ethereal aura.png", (self.width, self.height))
        if self.image is None:
            self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            pygame.draw.polygon(
                self.image, (100, 10, 10),
                [(self.width / 2, 0), (self.width, self.height), (0, self.height)],
            )
 
    def update(self, screen_rect):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if not self.entered and self.rect.colliderect(screen_rect):
            self.entered = True
 
    def is_offscreen(self, screen_rect):
        return (
            self.rect.top > screen_rect.bottom + 50
            or self.rect.bottom < screen_rect.top - 50
            or self.rect.left > screen_rect.right + 50
            or self.rect.right < screen_rect.left - 50
        )
 
    def draw(self, surf):
        rotated = pygame.transform.rotate(self.image, self.angle)
        rect = rotated.get_rect(center=self.rect.center)
        surf.blit(rotated, rect)
 
 
class Item:
    def __init__(self, screen_rect):
        self.width = 100
        self.height = 100
        self.rect = pygame.Rect(
            random.randint(100, screen_rect.right - 100),
            screen_rect.bottom - self.height - 150,
            self.width,
            self.height,
        )
        self.image = try_load_image(ASSET_PATH + "baogay.png", (self.width, self.height))
        if self.image is None:
            self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
            pygame.draw.circle(self.image, (255, 220, 0), (self.width // 2, self.height // 2), self.width // 2)
        self.blink_timer = 0
 
    def draw(self, surf):
        self.blink_timer += 1
        if (self.blink_timer // 15) % 2 == 0:
            surf.blit(self.image, self.rect)
 
 
# ================================================================
#  DRAW HELPERS
# ================================================================
 
def draw_warning(surf, direction, screen_rect, pos):
    size = 40
    padding = 30
    color = (255, 200, 80)
    if direction == "top":
        x = clamp(pos, padding + size, screen_rect.right - padding - size)
        pts = [(x, padding), (x - size, padding + size), (x + size, padding + size)]
    elif direction == "bottom":
        x = clamp(pos, padding + size, screen_rect.right - padding - size)
        pts = [(x, screen_rect.bottom - padding), (x - size, screen_rect.bottom - padding - size), (x + size, screen_rect.bottom - padding - size)]
    elif direction == "left":
        y = clamp(pos, padding + size, screen_rect.bottom - padding - size)
        pts = [(padding, y), (padding + size, y - size), (padding + size, y + size)]
    else:
        y = clamp(pos, padding + size, screen_rect.bottom - padding - size)
        pts = [(screen_rect.right - padding, y), (screen_rect.right - padding - size, y - size), (screen_rect.right - padding - size, y + size)]
    pygame.draw.polygon(surf, color, pts)
 
 
# ================================================================
#  GAME CHÍNH
# ================================================================
 
def run_game(screen, bg_image, char_index):
    clock = pygame.time.Clock()
    screen_rect = screen.get_rect()
 
    char_data = CHARACTERS[char_index]
    player = Player(screen_rect, char_data)
 
    projectiles = []
    score = 0
    running = True
    game_over = False
 
    projectile_speed = PROJECTILE_SPEED_START
    spawn_timer = 0
    spawn_interval = PROJECTILE_SPAWN_TIME
 
    item_timer = 0
    current_item = None
    invincible = False
    invincible_timer = 0
 
    anim_frames = [
        try_load_image(p, (SCREEN_WIDTH, SCREEN_HEIGHT))
        for p in char_data.get("anim_frames", [])
    ]
    use_image_anim = len(anim_frames) > 0
 
    anim_index = 0
    anim_timer = 0
    playing_anim = False
 
    try:
        voice_sound = pygame.mixer.Sound(ASSET_PATH + "Thoại-260402_175139.mp3")
        voice_sound.set_volume(1.0)
    except Exception:
        voice_sound = None
 
    while running:
        dt = clock.tick(FPS)
        spawn_timer += dt
 
        if not game_over:
            score += dt / 1000
            projectile_speed += PROJECTILE_ACCELERATION * (dt / 1000)
 
            item_timer += dt
            if item_timer >= ITEM_SPAWN_TIME and current_item is None and not invincible:
                item_timer = 0
                current_item = Item(screen_rect)
 
            if invincible:
                invincible_timer -= dt
                anim_timer += dt
                if anim_timer >= ANIM_FRAME_SPEED:
                    anim_timer = 0
                    total = len(anim_frames) if use_image_anim else 4
                    anim_index = (anim_index + 1) % total
                if invincible_timer <= 0:
                    invincible = False
                    playing_anim = False
 
            if current_item and player.rect.colliderect(current_item.rect):
                current_item = None
                invincible = True
                invincible_timer = ITEM_DURATION
                playing_anim = True
                anim_index = 0
                anim_timer = 0
                if voice_sound:
                    voice_sound.play()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "menu"   # ← quay về màn hình chọn nhân vật
                if game_over:
                    if event.key == pygame.K_r:
                        # Restart với cùng nhân vật
                        return "restart"
                    if event.key == pygame.K_m:
                        return "menu"
 
        keys = pygame.key.get_pressed()
        screen.blit(bg_image, (0, 0))
 
        if not game_over:
            player.update(keys, screen_rect, dt)
 
            if spawn_timer >= spawn_interval:
                spawn_timer = 0
                projectiles.append(Projectile(screen_rect, projectile_speed))
 
            for p in projectiles:
                p.update(screen_rect)
 
            projectiles = [p for p in projectiles if not p.is_offscreen(screen_rect)]
 
            for p in projectiles[:]:
                player_center = pygame.Rect(
                    player.rect.centerx - 5,
                    player.rect.centery - 80,
                    10,
                    160,
                )
                if p.rect.colliderect(player_center):
                    if player.parry_active or invincible:
                        projectiles.remove(p)
                        score += 1
                        continue
                    game_over = True
                    break
 
        for p in projectiles:
            if not p.entered:
                if p.direction in ("top", "bottom"):
                    draw_warning(screen, p.direction, screen_rect, p.rect.centerx)
                else:
                    draw_warning(screen, p.direction, screen_rect, p.rect.centery)
 
        for p in projectiles:
            p.draw(screen)
 
        if not playing_anim:
            player.draw(screen)
 
        if playing_anim:
            if use_image_anim:
                frame = anim_frames[anim_index % len(anim_frames)]
                if frame:
                    screen.blit(frame, (0, 0))
            else:
                # flash xanh fallback cho nhân vật chưa có anim
                flash = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
                alpha = [120, 80, 40, 80][anim_index % 4]
                flash.fill((50, 150, 255, alpha))
                screen.blit(flash, (0, 0))
 
        if current_item:
            current_item.draw(screen)
 
        draw_text(screen, f"Score: {int(score)}", 26, screen_rect.centerx - 60, 10)
        draw_text(screen, f"Nhân vật: {char_data['name']}", 22, 12, 10)
 
        if not game_over:
            if player.parry_cooldown > 0:
                draw_text(screen, f"Parry CD: {int(player.parry_cooldown)}ms", 22, 12, 40)
            else:
                draw_text(screen, "Parry: F", 22, 12, 40)
            draw_text(screen, "Jump: UP / W", 22, 12, 64)
            draw_text(screen, "ESC – Chọn nhân vật", 20, 12, 88, color=(180, 160, 110))
 
        if game_over:
            draw_text_centered(screen, "GAME OVER", 64, screen_rect.centerx, screen_rect.centery - 70, (230, 50, 50))
            draw_text_centered(screen, f"Score: {int(score)}", 36, screen_rect.centerx, screen_rect.centery + 50, (255, 220, 0))
            draw_text_centered(screen, "R – Chơi lại   |   M – Chọn nhân vật", 28,
                               screen_rect.centerx, screen_rect.centery + 10, (240, 240, 240))
 
        pygame.display.flip()
 
    return "quit"
 
 
# ================================================================
#  MAIN – vòng lặp menu → game → menu
# ================================================================
 
def main():
    pygame.init()
    pygame.mixer.init()
 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Ancient China Evade")
 
    bg_image = try_load_image(ASSET_PATH + "Không-Có-Tiêu-Đề244.png", (SCREEN_WIDTH, SCREEN_HEIGHT))
    if bg_image is None:
        bg_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        bg_image.fill((20, 30, 40))
 
    # Nhạc nền
    try:
        pygame.mixer.music.load(ASSET_PATH + "videoplayback.mp3")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
    except Exception:
        pass
 
    char_index = 0
 
    while True:
        # --- Màn hình chọn nhân vật ---
        selector = CharacterSelectScreen(screen, bg_image)
        char_index = selector.run()
 
        # --- Vòng lặp game (restart không cần chọn lại nhân vật) ---
        while True:
            result = run_game(screen, bg_image, char_index)
            if result == "restart":
                continue        # chơi lại cùng nhân vật
            elif result == "menu":
                break           # quay về màn hình chọn nhân vật
            else:               # "quit"
                pygame.quit()
                sys.exit()
 
 
if __name__ == "__main__":
    main()