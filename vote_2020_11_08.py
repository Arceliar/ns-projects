#!/usr/bin/env python2.7
from rrv_vote import getApprovedProjects

budget = 70.0  # million
costs = {
  'gridfinity': 3.0,
  'community': 26.0,
  'doublewallet': 40.0,
}
votes = []

# Neil
votes.append({
  'gridfinity': {
    # I continue to be impressed by the support that Gridfinity has shown to the PKT
    # project and their support and infrastructure has been somewhat critical to the
    # success of the project so far. In the past I have mentioned my concerns over how
    # ongoing support will be handled and funded on a long-term basis in the future,
    # but for now I am happy that this is adjacent to the success of the project.
    'short': 0.9,   #
    'long': 0.6,    #
    'scope': 0.5,   # 
    'risk': 0.7,    # 
    'hazard': 0.7   # 
  },

  'community': {
    # The pkt.cash website and promotional material so far have been very good overall
    # and further expansion in this space will be important in order to maintain any
    # external interest in the project. However, I am a little cautious about promises
    # made in the success criteria and whether the results will have longevity, hence
    # the risk.
    'short': 0.8,   # 
    'long': 0.5,    # 
    'scope': 0.6,   # 
    'risk': 0.4,    # 
    'hazard': 0.6   #
  },

  'doublewallet': {
    # I am encouraged by the idea of exploring more than one approach to off-chain
    # transactions as a way of hopefully improving chances of success, but if nothing
    # else then we will have more than one functioning PKT wallet as a result of this
    # work which is of obvious long term benefit.
    'short': 0.5,   # 
    'long': 0.8,    # 
    'scope': 0.8,   # 
    'risk': 0.7,    # 
    'hazard': 0.8   # 
  },
})

# Arceliar
votes.append({
  'gridfinity': {
    'short': 0.95,  # It's hard to think of something with more short-term benefit than ongoing tech support.
    'long': 0.5,    # A bug fixed now is a bug that doesn't need to be fixed later, so this has some long-term benefit, though I imagine the benefit to diminish after the proposal period ends (as people tend to stop caring about problems after they're no longer problems).
    'scope': 1.0,   # At 1.5 Mpkt per work-month, this is the most cost effective project submitted this round. I appreciate that payment is after each PR milestone, rather than up front.
    'risk': 0.95,   # I would be very surprised if this project fails to meet its stated goals (maybe +- the exact number of PRs submitted over the period, since some can be of dramatically larger scope than others, though 20/month or ~1/work-day doesn't seem unresonably high or low given the track record). Even in scenarios where it fails to meet all of it's goals (for some unforeseen reason), in contrast with the other proposals, some progress is better than none progress for this one, and the relatively short duration keeps the range of unforeseen problems fairly tightly bound.
    'hazard': 0.75  # The applicant is known by several NS members, but there really isn't anyone else qualified to do this (outside of CJD). Additionally, it's a very short duration commitment, and the cost-per-work-month is quite low compared to other proposals (with payment after-the-fact). These factors serve to mitigate some of the usual hazard penality I would normally be inclined to assign to a proposal from an applicant known to the NS.
  },

  'community': {
    'short': 0.8,   # The documentation side of the project is of significant short-term value to my mind, though I'm not entirely convinced that the material being suggested is appropriate to the kind of users who are likely to become active participants in the community given the current state of pkt as a whole.
    'long': 0.25,   #  The sorts of documentation being proposed is likely to become obsolete / be replaced over the long run, so eventually its significance seems likely to decrease off (IMO).
    'scope': 0.8,   # ~1.86 Mpkt per work-month, normalized against the most cost-effective project.
    'risk': 0.5,    # There's a (relatively) large team working on (relatively) many deliverables over a short time, so compared to the other projects (submitted this proposal period), this one seems less likely to meet all of it goals (and do so on time -- which is a consideration when a large fraction of the payment is requested in advance).
    'hazard': 0.0   # The success criteria (10x growth of chat/site-traffic/miners in 3 months) are unacceptable. We'd be spending pkt to quantifiably increase interest in pkt, the only directly foreseeable effect of which is to increase the value of pkt. This is isomorphic to a panzi scheme, so regardless of the applicant or the NS, it would be indefensible to fund such a project. More generally, any proposal that can be roughly summarized as "advertising" seems unacceptable regardless of success criteria.
  },

  'doublewallet': {
    'short': 0.75,  # A wallet is good, and two wallets does reduce the risk of complete failure, but it also means there's some duplicate effort (so the redundancy partly reduces some of the benefit).
    'long': 0.75,   # See above. Over all, having a good wallet is probably more important long-term than short term, but having *two* good wallets is probably less important (especially since at least one of them is more likely to become obsolete given the fact that, if pkt is successful enough for there to be a long term, then we're likely to see many more wallets be written over the years as new code bases emerge and platform market shares evolve).
    'scope': 0.375, # 4 Mpkt / person-month if we include pre-project effort (which seems reasonable to include), normalized against the most cost-effective proposal.
    'risk': 0.75,   # As with the community proposal, there's a relativley large amount of work to be done by a relatively large team (or two), over what seems like a relatively short duration considering the scope of the project. It seems somewhat likely that unforeseen problems will prevent at least some of the deliverables from being reached to the full satisfication of all parties by the target date, but this is partly mitigated by the pre-project effort and the fact that there are two wallets (so it's not the end of the world if some aspects of one don't pan out or take longer than expected).
    'hazard': 0.5   # The applicants are known to one or more NS members. While there are few people (if any) better positioned to write the OT/Rune wallet, I don't see the fact that it's an OT wallet being critical to fulfill the overall goal of the proposal (having one or two *good* wallet implementations, regardless of how they're implemented).
  },
})

print "WINNING PROJECTS: %s" % getApprovedProjects(budget, costs, votes)

projects = {}
for x in votes[0]:
    projects[x] = { 'short': 0., 'long': 0., 'scope': 0., 'risk': 0., 'hazard': 0. }
for r in votes:
    for x in r:
        ## x = repo, price_display, etc
        for y in projects[x]:
          projects[x][y] += r[x][y]
trans = {
    'short':  "Short term impact         ",
    'long':   "Long term impact          ",
    'scope':  "Scope and use of resources",
    'risk':   "Risk control              ",
    'hazard': "Hazard control            "
}
for p in projects:
    print p
    for q in projects[p]:
        print "  ", trans[q], projects[p][q]
