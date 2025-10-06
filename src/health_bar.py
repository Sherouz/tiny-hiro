# src/health_bar.py

# ===== Simplified health tracking (drawing handled by FancyUI) =====
class HealthBar:
    def __init__(self, entity):
        self.entity = entity
        self.max_value = entity.health_max
        self.current_value = entity.health

    # ----- Update current health -----
    def update(self):
        self.current_value = self.entity.health
        