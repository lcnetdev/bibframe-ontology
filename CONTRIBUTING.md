# Contributing

Please file issues in GitHub for problems or questions with the ontology.  No pull 
requests are accepted at this time.

Issues help capture the nature and scope of the problem and (ideally) provide 
space to recommend a change.

## Issue Examples

Examples can help to succinctly convey what is desired and/or needed to submit and 
best evaluate a request.  While the following examples are not perfect, they are nevertheless 
representative of the nature and tone of what is needed to assess an issue as a 
community.  One thing to take note of - specifically the two 'simpler' examples - 
is that given the nature of the request, sometimes
a short Issue is all that is really needed.

Nevertheless do, please, read the following sections of this document and not rely
exclusively on the examples.  The next section provides more context for the 
Examples and the "Prior Engagement and Experimentation" section offers 
additional strategies to embrace prior to submitting an issue.

Simpler examples:
- https://github.com/lcnetdev/bibframe-ontology/issues/78
- https://github.com/lcnetdev/bibframe-ontology/issues/75

More complex examples (for more complex issues):
- https://github.com/lcnetdev/bibframe-ontology/issues/76
- https://github.com/lcnetdev/bibframe-ontology/issues/77

## What makes a good GitHub Issue for the BF Vocabulary/Ontology?

A good GitHub issue will contain some narrative explanation of the problem and the 
need to address it with a Bibframe ontology change.  It should detail what about the 
current Bibframe vocabulary makes something impossible or not right.   If new classes 
and/or properties are proposed, suggested names should be provided along with a label, 
a definition, and any editorial notes.  If a new property is being proposed, include 
the type of property and any suggested domains and ranges.  If it is a Class, submit 
the type of class and whether it is a subclass of another Class. There should be examples 
showing the outcome of the proposed change, if applicable.   All of the changes that 
might be in play should be bundled under a single GitHub issue and discussed as a 
whole: for example, proposing an inverse to an existing property *and* asking to 
remove the domain/range of the existing property should not be treated as discrete 
requests. Thematically and functionally they are related. 

The ideas in the above stem from the current MARC change process, which, if you are not familiar,
takes the form first of "Discussion Papers" followed by "Proposals," if the discussion paper merits 
advancement.  A sample [Discussion Paper](https://www.loc.gov/marc/mac/2021/2021-dp09.html); a sample 
[Proposal](https://www.loc.gov/marc/mac/2021/2021-10.html).  To be clear, while an Issue that 
rose to the level of MARC Discussion Paper would be welcomed (they do introduce and lay out the issue 
comprehensively and clearly), GitHub issues do not need to be as polished, but the general 
outline - introduction of problem, current state, issues with current state, and solution - 
is essential to a good change process.

## Prior Engagement and Experimentation

It is assumed that any individual and/or organization requesting a change to the ontology be 
actually working with Bibframe data.  This is not an unreasonable expectation. 

Going further, experimentation before submitting change requests is encouraged.  There 
is certainly a time and place for theoretical requests (i.e. requests without prior practical 
implementation) but experimenting with something first establishes whether the solution worked 
and is worth keeping.  

LC, for example, uses what is commonly referred to as the bflc namespace for experimentation.  It 
is where LC minted the Hub class while experimenting with it for more than a year before 
promoting it to the main ontology.  LC has minted other properties and classes that it tests with, 
but which LC has not yet determined merit elevation.  It is also where LC creates properties that are 
needed locally but which may never be promoted to the main ontology. 

Real-life testing can strengthen a change request since it is made with some practical experience 
behind the proposal.  Bibframe is about actually encoding information in real life; it is not a 
conceptual model based on the theory of the ideal.  

## Other Communication

Please use the [Bibliographic Framework Transition Initiative Forum](mailto:BIBFRAME@LISTSERV.LOC.GOV) 
for general discussion, questions and feedback.  
