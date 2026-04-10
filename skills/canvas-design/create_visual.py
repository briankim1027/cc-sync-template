#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chromatic Infrastructure - Visual Expression
Telecommunications Market Analysis Visualization
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Rectangle, FancyBboxPatch, Wedge
import numpy as np
from pathlib import Path

# Set up the figure with precise dimensions
fig = plt.figure(figsize=(16, 20), dpi=300)
ax = plt.subplot(111)
ax.set_xlim(0, 100)
ax.set_ylim(0, 125)
ax.axis('off')
fig.patch.set_facecolor('#F8F8F6')
ax.set_facecolor('#F8F8F6')

# Color palette - Infrastructure chromatic system
COLOR_PRIMARY = '#2C5AA0'    # SKT Blue - dominance
COLOR_SECONDARY = '#E84A27'  # Opportunity Red
COLOR_TERTIARY = '#FFB81C'   # Connection Yellow
COLOR_ACCENT = '#00A896'     # Growth Teal
COLOR_NEUTRAL = '#4A4A4A'    # Text Gray
COLOR_BG_LIGHT = '#FFFFFF'

# ============================================================================
# TOP SECTION: Market Infrastructure (0-40 Y-axis)
# ============================================================================

# Title element - minimal, integrated
ax.text(8, 118, 'NETWORK', fontfamily='sans-serif', fontsize=48,
        fontweight=300, color=COLOR_NEUTRAL, ha='left', va='top')

ax.text(8, 112, 'SYNTHESIS', fontfamily='sans-serif', fontsize=48,
        fontweight=700, color=COLOR_PRIMARY, ha='left', va='top')

# Subtitle - data label
ax.text(8, 107, '전북특별자치도 · 다문화 네트워크 분석',
        fontfamily='sans-serif', fontsize=11, fontweight=300,
        color=COLOR_NEUTRAL, ha='left', va='top', alpha=0.7)

# ============================================================================
# SECTION 1: Market Share Visualization (Y: 75-100)
# ============================================================================

# Market share bars - horizontal infrastructure
y_start = 95
bar_height = 4
spacing = 6.5

# SKT - 40.4%
rect1 = Rectangle((8, y_start), 40.4, bar_height,
                  facecolor=COLOR_PRIMARY, edgecolor='none', alpha=0.9)
ax.add_patch(rect1)
ax.text(49, y_start + bar_height/2, '40.4%', fontfamily='sans-serif',
        fontsize=9, fontweight=600, color=COLOR_PRIMARY,
        ha='left', va='center')
ax.text(6, y_start + bar_height/2, 'SKT', fontfamily='sans-serif',
        fontsize=8, fontweight=400, color=COLOR_NEUTRAL,
        ha='right', va='center', alpha=0.6)

# KT - 29.7%
y_pos = y_start - spacing
rect2 = Rectangle((8, y_pos), 29.7, bar_height,
                  facecolor=COLOR_NEUTRAL, edgecolor='none', alpha=0.3)
ax.add_patch(rect2)
ax.text(38.2, y_pos + bar_height/2, '29.7%', fontfamily='sans-serif',
        fontsize=9, fontweight=400, color=COLOR_NEUTRAL,
        ha='left', va='center', alpha=0.6)
ax.text(6, y_pos + bar_height/2, 'KT', fontfamily='sans-serif',
        fontsize=8, fontweight=400, color=COLOR_NEUTRAL,
        ha='right', va='center', alpha=0.6)

# LG U+ - 29.9%
y_pos = y_start - spacing * 2
rect3 = Rectangle((8, y_pos), 29.9, bar_height,
                  facecolor=COLOR_NEUTRAL, edgecolor='none', alpha=0.3)
ax.add_patch(rect3)
ax.text(38.4, y_pos + bar_height/2, '29.9%', fontfamily='sans-serif',
        fontsize=9, fontweight=400, color=COLOR_NEUTRAL,
        ha='left', va='center', alpha=0.6)
ax.text(6, y_pos + bar_height/2, 'LG U+', fontfamily='sans-serif',
        fontsize=8, fontweight=400, color=COLOR_NEUTRAL,
        ha='right', va='center', alpha=0.6)

# Section label
ax.text(8, 103, 'MARKET INFRASTRUCTURE', fontfamily='sans-serif',
        fontsize=7, fontweight=600, color=COLOR_NEUTRAL,
        ha='left', va='bottom', alpha=0.5)

# ============================================================================
# SECTION 2: Demographic Nodes (Y: 50-72)
# ============================================================================

# Section label
ax.text(8, 72, 'DEMOGRAPHIC NETWORKS', fontfamily='sans-serif',
        fontsize=7, fontweight=600, color=COLOR_NEUTRAL,
        ha='left', va='bottom', alpha=0.5)

# Central circle - Total multicultural families (represents national scale)
center_x, center_y = 30, 60
radius = 10
circle_main = Circle((center_x, center_y), radius,
                     facecolor=COLOR_ACCENT, edgecolor='none', alpha=0.15)
ax.add_patch(circle_main)

circle_main_ring = Circle((center_x, center_y), radius,
                         facecolor='none', edgecolor=COLOR_ACCENT,
                         linewidth=2, alpha=0.8)
ax.add_patch(circle_main_ring)

# Inner data
ax.text(center_x, center_y + 2, '1.19M', fontfamily='sans-serif',
        fontsize=14, fontweight=700, color=COLOR_ACCENT,
        ha='center', va='center')
ax.text(center_x, center_y - 3, '다문화 인구', fontfamily='sans-serif',
        fontsize=8, fontweight=300, color=COLOR_ACCENT,
        ha='center', va='center', alpha=0.7)

# Satellite nodes - Regional distribution
satellite_positions = [
    (55, 65, 4, '전북', COLOR_PRIMARY),
    (55, 55, 3.5, '서울', COLOR_NEUTRAL),
    (70, 60, 3, '경기', COLOR_NEUTRAL),
    (48, 48, 2.5, '부산', COLOR_NEUTRAL),
]

for x, y, r, label, color in satellite_positions:
    circle = Circle((x, y), r, facecolor=color, edgecolor='none',
                   alpha=0.3 if color == COLOR_NEUTRAL else 0.6)
    ax.add_patch(circle)
    ax.text(x, y, label, fontfamily='sans-serif', fontsize=6,
            fontweight=500, color=color, ha='center', va='center',
            alpha=0.8)

    # Connection lines to center
    if label == '전북':
        ax.plot([center_x + radius * 0.7, x - r * 0.7],
               [center_y, y], color=COLOR_PRIMARY,
               linewidth=1.5, alpha=0.4, linestyle='-')

# ============================================================================
# SECTION 3: Opportunity Matrix (Y: 15-45)
# ============================================================================

# Section label
ax.text(8, 45, 'STRATEGIC OPPORTUNITIES', fontfamily='sans-serif',
        fontsize=7, fontweight=600, color=COLOR_NEUTRAL,
        ha='left', va='bottom', alpha=0.5)

# Grid-based opportunity zones
opportunity_data = [
    {'x': 10, 'y': 35, 'w': 25, 'h': 7, 'label': '다국어 고객지원',
     'value': '85', 'color': COLOR_SECONDARY},
    {'x': 37, 'y': 35, 'w': 25, 'h': 7, 'label': '가족 결합 할인',
     'value': '72', 'color': COLOR_TERTIARY},
    {'x': 64, 'y': 35, 'w': 25, 'h': 7, 'label': '커뮤니티 파트너십',
     'value': '68', 'color': COLOR_ACCENT},
    {'x': 10, 'y': 26, 'w': 25, 'h': 7, 'label': '인터넷 요금 지원',
     'value': '78', 'color': COLOR_PRIMARY},
    {'x': 37, 'y': 26, 'w': 25, 'h': 7, 'label': '국제 로밍 패키지',
     'value': '81', 'color': COLOR_SECONDARY},
    {'x': 64, 'y': 26, 'w': 25, 'h': 7, 'label': '다문화 센터 연계',
     'value': '76', 'color': COLOR_TERTIARY},
]

for opp in opportunity_data:
    # Opportunity strength visualization
    strength_width = opp['w'] * (int(opp['value']) / 100)

    # Background
    rect_bg = Rectangle((opp['x'], opp['y']), opp['w'], opp['h'],
                        facecolor=COLOR_BG_LIGHT, edgecolor=opp['color'],
                        linewidth=0.5, alpha=0.3)
    ax.add_patch(rect_bg)

    # Strength indicator
    rect_strength = Rectangle((opp['x'], opp['y']), strength_width, opp['h'],
                              facecolor=opp['color'], edgecolor='none', alpha=0.25)
    ax.add_patch(rect_strength)

    # Label
    ax.text(opp['x'] + opp['w']/2, opp['y'] + opp['h']/2 + 1,
            opp['label'], fontfamily='sans-serif', fontsize=7,
            fontweight=500, color=COLOR_NEUTRAL, ha='center', va='center')

    # Value
    ax.text(opp['x'] + opp['w']/2, opp['y'] + opp['h']/2 - 1.5,
            opp['value'], fontfamily='sans-serif', fontsize=9,
            fontweight=700, color=opp['color'], ha='center', va='center',
            alpha=0.8)

# ============================================================================
# SECTION 4: Key Insight - Bottom
# ============================================================================

# Key metric callout
callout_y = 12
ax.text(8, callout_y, '202K', fontfamily='sans-serif', fontsize=32,
        fontweight=700, color=COLOR_PRIMARY, ha='left', va='center')
ax.text(30, callout_y, '다문화 학생 (2025)', fontfamily='sans-serif',
        fontsize=10, fontweight=300, color=COLOR_NEUTRAL,
        ha='left', va='center', alpha=0.7)

# Growth indicator
growth_arrow = patches.FancyArrowPatch((56, callout_y - 1), (65, callout_y - 1),
                                      arrowstyle='->', mutation_scale=15,
                                      color=COLOR_ACCENT, linewidth=2, alpha=0.6)
ax.add_patch(growth_arrow)
ax.text(70, callout_y, '+59% (5년)', fontfamily='sans-serif', fontsize=9,
        fontweight=600, color=COLOR_ACCENT, ha='left', va='center')

# ============================================================================
# Footer metadata
# ============================================================================

ax.text(8, 3, '2024 전국 다문화가족 실태조사 · 통신시장 분석 데이터',
        fontfamily='sans-serif', fontsize=6, fontweight=300,
        color=COLOR_NEUTRAL, ha='left', va='bottom', alpha=0.5)

ax.text(92, 3, 'INFRASTRUCTURE ANALYSIS',
        fontfamily='sans-serif', fontsize=6, fontweight=400,
        color=COLOR_NEUTRAL, ha='right', va='bottom', alpha=0.4)

# ============================================================================
# Final polish: Add subtle grid system markers
# ============================================================================

# Vertical guides (subtle)
for x in [8, 35, 62, 89]:
    ax.plot([x, x], [10, 105], color=COLOR_NEUTRAL,
           linewidth=0.3, alpha=0.1, linestyle='-')

# Save with high quality
plt.tight_layout(pad=0.5)
output_path = Path('C:/Users/c/.claude/skills/canvas-design/chromatic-infrastructure-telecom.pdf')
plt.savefig(output_path, format='pdf', dpi=300, bbox_inches='tight',
            facecolor='#F8F8F6', edgecolor='none')

# Also save as PNG
output_png = Path('C:/Users/c/.claude/skills/canvas-design/chromatic-infrastructure-telecom.png')
plt.savefig(output_png, format='png', dpi=300, bbox_inches='tight',
            facecolor='#F8F8F6', edgecolor='none')

print(f"✓ PDF saved: {output_path}")
print(f"✓ PNG saved: {output_png}")

plt.close()
