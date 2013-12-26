/**
 * jQuery.jBackground
 * 
 * 1.0.0
 * 
 * João Machado
 * 
 * http://code.google.com/p/jbackground/
 * 
 */

/**
 * 
 * A fork of jQuery.jParallax
 * 
 * 0.9.1
 * 
 * Stephen Band
 * 
 * http://webdev.stephband.info/parallax.html
 * 
 */
(function(jQuery) {

	// PRIVATE FUNCTIONS

	function initOrigin(l) {

		if (l.xorigin == 'left') {
			l.xorigin = 0;
		} else if (l.xorigin == 'middle' || l.xorigin == 'centre' || l.xorigin == 'center') {
			l.xorigin = 0.5;
		} else if (l.xorigin == 'right') {
			l.xorigin = 1;
		}
		if (l.yorigin == 'top') {
			l.yorigin = 0;
		} else if (l.yorigin == 'middle' || l.yorigin == 'centre' || l.yorigin == 'center') {
			l.yorigin = 0.5;
		} else if (l.yorigin == 'bottom') {
			l.yorigin = 1;
		}
	}

	function positionMouse(mouseport, localmouse, virtualmouse) {

		var difference = {
			x : 0,
			y : 0,
			sum : 0
		};

		// Calculate difference
		difference.x = virtualmouse.x - localmouse.x;
		difference.y = virtualmouse.y - localmouse.y;
		difference.sum = Math.sqrt(difference.x * difference.x + difference.y * difference.y);

		// Reset virtualmouse
		virtualmouse.x = localmouse.x + difference.x * mouseport.takeoverFactor;
		virtualmouse.y = localmouse.y + difference.y * mouseport.takeoverFactor;

		// If mouse is inside the takeoverThresh set ontarget to true
		if (difference.sum < mouseport.takeoverThresh && difference.sum > mouseport.takeoverThresh * -1) {
			mouseport.ontarget = true;
		} else {
			mouseport.ontarget = false;
		}
	}

	function setupPorts(viewport, mouseport) {

		var offset = mouseport.element.offset();

		jQuery.extend(viewport, {
			width : viewport.element.width(),
			height : viewport.element.height()
		});

		jQuery.extend(mouseport, {
			width : mouseport.element.width(),
			height : mouseport.element.height(),
			top : offset.top,
			left : offset.left
		});
	}

	function moveLayers(layer, xratio, yratio) {

		var xpos;
		var ypos;
		var cssObject;

		// Calculate the moving factor
		xpos = layer.xtravel * xratio;
		ypos = layer.ytravel * yratio;

		cssObject = {};
		// Do the moving by pixels or by ratio depending on travelpx
		if (layer.xparallax) {
			cssObject.bgx = xpos * layer.element.width() / layer.element.width() * 100 + '%';
		}
		if (layer.yparallax) {
			cssObject.bgy = ypos * layer.element.height() / layer.element.height() * 100 + '%';
		}
		layer.element.css( {
			backgroundPosition : cssObject.bgx + ' ' + cssObject.bgy
		});

	}

	// PLUGIN DEFINITION
	// **********************************************************************

	jQuery.fn.jbackground = function(options) {

		// Organise settings into objects (Is this a bit of a mess, or is it
		// efficient?)
		var settings = jQuery().extend( {}, jQuery.fn.jbackground.settings, options);
		var settingsLayer = {
			xparallax : settings.xparallax,
			yparallax : settings.yparallax,
			xorigin : settings.xorigin,
			yorigin : settings.yorigin,
			xtravel : settings.xtravel,
			ytravel : settings.ytravel
		};
		var settingsMouseport = {
			element : settings.mouseport,
			takeoverFactor : settings.takeoverFactor,
			takeoverThresh : settings.takeoverThresh
		};
		if (settings.mouseport)
			settingsMouseport['element'] = settings.mouseport;

		// Iterate matched elements
		return this.each(function() {
			// VAR

				var localmouse = {
					x : 0.5,
					y : 0.5
				};

				var virtualmouse = {
					x : 0.5,
					y : 0.5
				};

				var timer = {
					running : false,
					frame : settings.frameDuration,
					fire : function(x, y) {

						positionMouse(mouseport, localmouse, virtualmouse);

						moveLayers(layer, virtualmouse.x, virtualmouse.y);

						this.running = setTimeout(function() {

							if (localmouse.x != x || localmouse.y != y || !mouseport.ontarget) {

								timer.fire(localmouse.x, localmouse.y);

							} else if (timer.running) {

								timer.running = false;

							}
						}, timer.frame);
					}
				};

				var viewport = {
					element : jQuery(this)
				};

				var mouseport = jQuery.extend( {}, {
					element : viewport.element
				}, settingsMouseport, {
					xinside : false, // is the mouse inside the mouseport's dimensions?
					yinside : false,
					active : false, // are the mouse coordinates still being read?
					ontarget : false
				// is the top layer inside the takeoverThresh?
						});

				var layer;

				// RUN

				setupPorts(viewport, mouseport);

				// Create layer from settings if it doesn't exist
				layer = jQuery.extend( {}, settingsLayer, {
					element : viewport.element
				});

				moveLayers(layer, 0.5, 0.5);

				// Mouse Response
				if (settings.mouseResponse) {
					jQuery().mousemove(function(mouse) {

						// Is mouse inside?
							mouseport.xinside = (mouse.pageX >= mouseport.left && mouse.pageX < mouseport.width + mouseport.left) ? true : false;
							mouseport.yinside = (mouse.pageY >= mouseport.top && mouse.pageY < mouseport.height + mouseport.top) ? true : false;
							// Then switch active on.
							if (mouseport.xinside && mouseport.yinside && !mouseport.active) {
								mouseport.ontarget = false;
								mouseport.active = true;
							}
							// If active is on give localmouse
							// coordinates
							if (mouseport.active) {
								if (mouseport.xinside) {
									localmouse.x = (mouse.pageX - mouseport.left) / mouseport.width;
								} else {
									localmouse.x = (mouse.pageX < mouseport.left) ? 0 : 1;
								}
								if (mouseport.yinside) {
									localmouse.y = (mouse.pageY - mouseport.top) / mouseport.height;
								} else {
									localmouse.y = (mouse.pageY < mouseport.top) ? 0 : 1;
								}
							}

							// If mouse is inside, fire timer
							if (mouseport.xinside && mouseport.yinside) {
								if (!timer.running) {
									timer.fire(localmouse.x, localmouse.y);
								}
							} else if (mouseport.active) {
								mouseport.active = false;
							}
						});
				}

				// Window Resize Response
				jQuery(window).resize(function() {

					setupPorts(viewport, mouseport);

					layer = jQuery.extend( {}, settingsLayer, {
						element : viewport.element
					});

				});

			});
	};

	// END OF PLUGIN DEFINITION
	// **********************************************************************

	// PLUGIN DEFAULTS

	jQuery.fn.jbackground.settings = {
		mouseResponse : true, // Sets mouse response
		xparallax : true, // Sets directions to move in
		yparallax : true, //
		xorigin : 0.5, // Sets default alignment - only comes into play when travel is not 1
		yorigin : 0.5, //
		xtravel : 1, // Factor by which travel is amplified
		ytravel : 1, //
		takeoverFactor : 0.62, // Sets rate of decay curve for catching up with target mouse position
		takeoverThresh : 0.002, // Sets the distance within which virtualmouse is considered to be on target, as a multiple of mouseport width.
		frameDuration : 25
	// In milliseconds
	};

	// RUN

	initOrigin(jQuery.fn.jbackground.settings);

})(jQuery);