<?php

class html_element {
/* http://davidwalsh.name/create-html-elements-php-htmlelement-class */
/* creates an html element, like in js */
    /* vars */
    var $type;
    var $attributes;
    var $self_closers;

    /* constructor */
    function html_element($type,
                          $self_closers = array('input','img','hr','br','meta','link')) {
        $this->type = strtolower($type);
        $this->self_closers = $self_closers;
    }

    function get($attribute) {
        return $this->attributes[$attribute];
    }

    function set($attribute,
                 $value = '') {
        if(!is_array($attribute)) {
            $this->attributes[$attribute] = $value;
        }
        else {
            $this->attributes = array_merge($this->attributes,$attribute);
        }
    }

    function remove($attribute) {
        if(isset($this->attributes[$attribute])) {
            unset($this->attributes[$attribute]);
        }
    }

    function clear() {
        $this->attributes = array();
    }

    function inject($object) {
/*
    Daniel Philips mod from comment on same page.
    Original produces "undefined index text" errors
*/
        if(!isset($this->attributes['text'])) {
            $this->attributes['text'] = $object->build();
        }
        else {
            $this->attributes['text'].= $object->build();
        }
    }

    function build() {
        if(!isset($this->attributes['text'])) {
            $this->attributes['text']=''; /* phrits's hack */
        }
        //start
        $build = '<'.$this->type;

        //add attributes
        if(count($this->attributes)) {
            foreach($this->attributes as $key=>$value) {
                if($key != 'text') { $build.= ' '.$key.'="'.$value.'"'; }
            }
        }

        //closing
        if(!in_array($this->type,$this->self_closers)) {
            $build .= '>'.$this->attributes['text']. '</'.$this->type.'>';
        }
        else {
            $build .= ' />';
        }

        //return it
        return $build;
    }

    function output() {
        echo $this->build();
    }
}

function curPageURL() {
/* http://webcheatsheet.com/php/get_current_page_url.php */
 $pageURL = 'http';
if (!empty($_SERVER['HTTPS'])) {$pageURL .= "s";}   /* http://www.codingforums.com/showthread.php?t=173189 */
 $pageURL .= "://";
 if ($_SERVER["SERVER_PORT"] != "80") {
  $pageURL .= $_SERVER["SERVER_NAME"].":".$_SERVER["SERVER_PORT"].$_SERVER["REQUEST_URI"];
 } else {
  $pageURL .= $_SERVER["SERVER_NAME"].$_SERVER["REQUEST_URI"];
 }
 return $pageURL;
}

function doctype() {
    ?>
    <!DOCTYPE html>
    <?php
}
function html_link($attributes) {
/* E.g., CSS */
    $link = new html_element('link');
    foreach ($attributes as $attribute => $value) {
        $link->set($attribute, $value);
    }
    $link->output();
}
function html_meta($attributes = array()) {
/* E.g., keywords, etc. */
    $meta = new html_element('meta');
    foreach ($attributes as $attribute => $value) {
        $meta->set("name", $attribute);
        $meta->set("content", $value);
    }
    $meta->output();
}

function html_p($text = '', $class='') {
    $p = new html_element('p');
    $p->set('text', $text);
    if($class) {
        $p->set('class', $class);
    }
    return $p;
}

function html_span($text = '', $class = '') {
    $span = new html_element('span');
    $span->set('text', $text);
    if($class) {
        $span->set('class', $class);
    }
    return $span;
}

function html_simple($type = 'div', $text = '', $class = '') {
    $html = new html_element($type);
    $html->set('text', $text);
    if($class) {
        $html->set('class', $class);
    }
    return $html;
}

function para($text = '', $class = '') {
    $para = new html_element('p');
    $para->set('text', $text);
    if($class) {
        $para->set('class', $class);
    }
    return $para->build();
}
function span($text = '', $class = '') {
    $span = new html_element('span');
    $span->set('text', $text);
    if($class) {
        $span->set('class', $class);
    }
    return $span->build();
}

function anchor($text = '', $url = '', $class='') {
    $anchor = new html_element('a');
    if($text) {
        $anchor->set('text', $text);
    }
    if($url) {
        $anchor->set('href', $url);
    }
    if($class) {
        $anchor->set('class', $class);
    }
    return $anchor->build();
}




function link_mailto(   $text = 'mailto:phrits',
                        $address = 'mailto@phrits.com',
                        $subject = 'Change this Subject Line or your message will be filtered out as Spam.',
                        $class = '') {
    $anchor = new html_element('a');
    $href = "mailto:" . $address . "?subject=" . $subject;
    $anchor->set('href', $href);
    $anchor->set('text', $text);
    if($class) {
        $anchor->set('class', $class);
    }
    return $anchor->build();
}

function link_home() {
    $anchor = new html_element('a');
    $anchor->set('class', "phrits");
    $anchor->set('href',"https://phrits.com/");
    $anchor->set('text',"phrits.com");
    $anchor->set('title',"phrits.com");
    return $anchor->build();
}

function description($text = '') {
    html_meta(array("description"      => "$text"));
}

?>
