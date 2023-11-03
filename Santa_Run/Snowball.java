import greenfoot.*;  // (World, Actor, GreenfootImage, Greenfoot and MouseInfo)

/**
 * Write a description of class Snowball here.
 * 
 * @author (your name) 
 * @version (a version number or a date)
 */
public class Snowball extends Actor
{
    /** A bullet looses one life each act, and will disappear when life = 0 */
    private int life = 100;
    public Snowball(int speed)
    {
        super();
    }
    public void act()
    {
        if(life <= 0)
        {
            getWorld().removeObject(this);
        } 
        else
          {
            move(8);
            life--;
            Robot robot = (Robot) getOneIntersectingObject(Robot.class);
           if (robot != null)
          {
            removeTouching(Robot.class);
            MyWorld myWorld = (MyWorld)getWorld();
            myWorld.addScore(20);
            getWorld().removeObject(this);
          }
        }
      }
    }
