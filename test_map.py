import pytest
import map

def test_obstacle_amt():
    obst_amt = 10
    obst_map = map.Map(200, 200, obst_amt, 0)
    assert len(obst_map.obstacles) == obst_amt

def test_waypoint_amt():
    wp_amt = 10
    wp_map = map.Map(200, 200, 0, wp_amt)
    assert len(wp_map.waypoints) == wp_amt

def test_collides_true():
    col_map = map.Map(200, 200, 1, 0)
    obst_location = (col_map.obstacles[0][0], col_map.obstacles[0][1])
    assert col_map.collides(obst_location)

def test_collides_false():
    col_map = map.Map(200, 200, 1, 0)
    safe_radius = 1 + col_map.obstacles[0][2]
    clear_location = (col_map.obstacles[0][0] + safe_radius, col_map.obstacles[0][1] + safe_radius)
    assert not col_map.collides(clear_location)

def test_waypoint_noncollide():
    wp_map = map.Map(200, 200, 3, 10)
    for wp in wp_map.waypoints:
        assert not wp_map.collides(wp)
